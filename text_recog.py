<<<<<<< HEAD
from paddleocr import PaddleOCR
import cv2

cus_ocr = PaddleOCR(use_gpu = False, use_angle_cls = True, det_model_dir=r"C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\output\det_pse_inference")

img_path = r'C:\Users\Admin\Documents\Khoa_Luan_Code\test_image\VAIPE_P_TRAIN_828.png'

image_cv = cv2.imread(img_path)

result = cus_ocr.ocr(img_path)[0]
# print(result)

boxes = [line[0] for line in result]
# texts = [line[1][0] for line in result]

img_cop = image_cv.copy()

for box in boxes:
    cv2.rectangle(img_cop, (int(box[0][0]), int(box[0][1]), int(box[2][0]), int(box[2][1])),(0,0,255),1)
    
# cv2.imwrite(r"C:\Users\Admin\Documents\Khoa_Luan_Code\result_image\detect1.jpg", img_cop)
cv2.imshow("dec", img_cop)
cv2.waitKey(0)
=======
from paddleocr import PaddleOCR
import cv2

cus_ocr = PaddleOCR(use_gpu = False, use_angle_cls = True, det_model_dir=r"C:\Users\Admin\Documents\Khoa_Luan_Code\PaddleOCR\PaddleOCR\output\det_pse_inference")

img_path = r'C:\Users\Admin\Documents\Khoa_Luan_Code\test_image\VAIPE_P_TRAIN_828.png'

image_cv = cv2.imread(img_path)

result = cus_ocr.ocr(img_path)[0]
# print(result)

boxes = [line[0] for line in result]
# texts = [line[1][0] for line in result]

img_cop = image_cv.copy()

for box in boxes:
    cv2.rectangle(img_cop, (int(box[0][0]), int(box[0][1]), int(box[2][0]), int(box[2][1])),(0,0,255),1)
    
# cv2.imwrite(r"C:\Users\Admin\Documents\Khoa_Luan_Code\result_image\detect1.jpg", img_cop)
cv2.imshow("dec", img_cop)
cv2.waitKey(0)
>>>>>>> ddfcb7004e7c2ef5f5763c85de7b1cc2ce6b1345
cv2.destroyAllWindows()