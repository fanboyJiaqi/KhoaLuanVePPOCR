from paddleocr import PaddleOCR
import cv2
import os

# Cấu hình OCR
cus_ocr = PaddleOCR(use_gpu=False, use_angle_cls=True, det_model_dir=r"C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\inference\det_pse")

# Đường dẫn thư mục ảnh đầu vào và đầu ra
input_dir = r'C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\image_test'
output_dir = r'C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\result_image'

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Duyệt qua từng ảnh trong thư mục input_dir
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    
    # Đọc ảnh
    image_cv = cv2.imread(img_path)
    
    # Phát hiện văn bản
    result = cus_ocr.ocr(img_path)[0]
    
    # Lấy các hộp văn bản
    boxes = [line[0] for line in result]
    
    # Sao chép ảnh để vẽ hộp
    img_cop = image_cv.copy()
    
    # Vẽ hộp lên ảnh
    for box in boxes:
        cv2.rectangle(img_cop, (int(box[0][0]), int(box[0][1])), (int(box[2][0]), int(box[2][1])), (0, 0, 255), 1)
    
    # Lưu ảnh đã vẽ hộp vào thư mục output_dir
    output_path = os.path.join(output_dir, img_name)
    cv2.imwrite(output_path, img_cop)

print("Hoàn thành phát hiện văn bản và lưu ảnh kết quả.")
