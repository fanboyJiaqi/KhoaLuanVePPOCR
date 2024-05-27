<<<<<<< HEAD
from augraphy import *
import cv2

image = cv2.imread(r'C:\Users\Admin\Documents\Khoa_Luan_Code\test_image\VAIPE_P_TRAIN_826.png')


pp_line = Faxify()

au_img = pp_line(image)

cv2.imwrite(r'C:\Users\Admin\Documents\Khoa_Luan_Code\test_image\Faxify_826.png',au_img)
=======
from augraphy import *
import cv2

image = cv2.imread(r'C:\Users\Admin\Documents\Khoa_Luan_Code\test_image\VAIPE_P_TRAIN_826.png')


pp_line = Faxify()

au_img = pp_line(image)

cv2.imwrite(r'C:\Users\Admin\Documents\Khoa_Luan_Code\test_image\Faxify_826.png',au_img)
>>>>>>> ddfcb7004e7c2ef5f5763c85de7b1cc2ce6b1345
