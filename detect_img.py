from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(use_angle_cls=True, det_model_dir='output/det_db_inference', use_gpu=False)
image_path = ('/home/phuong/Documents/Khoa_Luan_Data_Label/images/VAIPE_P_TRAIN_936.png')

image_cv = cv2.imread(image_path)

output = ocr.ocr(image_cv)[0]

print(output)

boxes = [line[0] for line in output]

img_cop = image_cv.copy()

for box in boxes:
    cv2.rectangle(img_cop, (int(box[0][0]), int(box[0][1])), (int(box[2][0]), int(box[2][1])), (0, 0, 255), 2)

cv2.imwrite("detect.jpg", img_cop)
cv2.waitKey(0)
cv2.destroyAllWindows()
