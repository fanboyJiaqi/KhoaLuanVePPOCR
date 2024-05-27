import json
from paddleocr import PaddleOCR
import cv2
import os

def compute_iou(box1, box2):
    x1_max = max(box1[0], box2[0])
    y1_max = max(box1[1], box2[1])
    x2_min = min(box1[2], box2[2])
    y2_min = min(box1[3], box2[3])

    inter_area = max(0, x2_min - x1_max + 1) * max(0, y2_min - y1_max + 1)
    
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
    
    iou = inter_area / float(box1_area + box2_area - inter_area)
    
    return iou

def load_ground_truth(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        gt_data = json.load(file)
    gt_boxes = [item['box'] for item in gt_data]
    return gt_boxes

def convert_quad_to_box(quad):
    x_coords = [point[0] for point in quad]
    y_coords = [point[1] for point in quad]
    return [min(x_coords), min(y_coords), max(x_coords), max(y_coords)]

# Cấu hình OCR
cus_ocr = PaddleOCR(use_gpu=False, use_angle_cls=True, det_model_dir=r"C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\inference\det_pse")

# Đường dẫn thư mục ảnh đầu vào và ground truth
input_dir = r'C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\image_test'
gt_dir = r'C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\gt_dir'

# Tính Precision, Recall và F1-score
true_positives = 0
false_positives = 0
false_negatives = 0

for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    
    # Đọc ảnh
    image_cv = cv2.imread(img_path)
    
    # Phát hiện văn bản
    result = cus_ocr.ocr(img_path)[0]
    
    # Lấy các hộp văn bản dự đoán và chuyển đổi từ tứ giác sang hộp bao quanh dạng [x1, y1, x2, y2]
    pred_boxes = [convert_quad_to_box(line[0]) for line in result]
    
    # Lấy các hộp văn bản ground truth
    gt_path = os.path.join(gt_dir, img_name.replace('.png', '.json'))  # Giả sử ground truth được lưu dưới dạng .json
    gt_boxes = load_ground_truth(gt_path)
    
    # So khớp các hộp
    matched = set()
    for pred_box in pred_boxes:
        ious = [compute_iou(pred_box, gt_box) for gt_box in gt_boxes]
        best_iou = max(ious) if ious else 0
        if best_iou > 0.5:
            true_positives += 1
            matched.add(ious.index(best_iou))
        else:
            false_positives += 1

    false_negatives += len(gt_boxes) - len(matched)

precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1-score: {f1_score:.4f}')
