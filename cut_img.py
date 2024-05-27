<<<<<<< HEAD
from PIL import Image, ImageDraw
import cv2
import numpy as np
import os
from tqdm import tqdm
from convert import read_convert_label_file
from sklearn.model_selection import train_test_split

file_path = "/home/phuong/PaddleOCR/dataset/Data_Detec_Train/Augraphy_ColorPaper_Image/Label.txt"
info = read_convert_label_file(file_path)


def crop_img(info):
    data = []
    for i in info:
        for j in i[1]:
            data.append([i[0], j['transcription'], j['points']])
        break
    print(len(data))
    for img in data:
        coordinates = img
        print(coordinates)
        # coordinates = [tuple(sublist) for sublist in coordinates]
        # print(coordinates)

        # cropped_image = crop_polygon(info[219][0], coordinates)
        # cropped_image.show()

def crop_polygon(image, polygon_points):
    # image = Image.open(image_path)
    polygon_points = [tuple(sublist) for sublist in polygon_points]
    mask = Image.new('L', image.size, 0)
    ImageDraw.Draw(mask).polygon(polygon_points, outline=None, fill=255)
    
    cropped_image = Image.composite(image, Image.new('RGB', image.size, (255, 255, 255)), mask)
    cropped_image = cropped_image.crop(mask.getbbox())
    
    return cropped_image

def split_bounding_boxes(info, save_dir, label_name):

    os.makedirs(save_dir, exist_ok=True)
    img_sava_dir = os.path.join(save_dir, label_name)
    os.makedirs(img_sava_dir, exist_ok=True)

    count = 0
    labels = []
    for imgs in tqdm(info):
        img = Image.open(imgs[0])

        for label_bb in imgs[1]:
            label = label_bb['transcription']
            bb = label_bb['points']
            cropped_img = crop_polygon(img, bb)

            # Bỏ qua trường hợp 90% nội dung ảnh cắt là màu trắng hoặc đen.
            # if np.mean(cropped_img) < 35 or np.mean(cropped_img) > 220:
            #     continue

            # Bỏ qua trường hợp ảnh cắt có width < 10 hoặc heigh < 10
            # if cropped_img.size[0] < 10 or cropped_img.size[1] < 10:
            #     continue

            # Tạo tên cho file ảnh đã cắt và lưu vào save_dir
            filename = f"{count:06d}.jpg"
            cropped_img.save(os.path.join(img_sava_dir + '', filename))

            new_img_path = os.path.join(img_sava_dir, filename)

            # Đưa format label mới vào list labels
            # Format: img_path\tlabel
            label = new_img_path + '\t' + label

            labels.append(label)  # Append label to the list

            count += 1
        # break

    print(f"Created {count} images")

    # Đưa list labels vào file labels.txt
    with open(os.path.join(save_dir, 'rec_gt_'+label_name+'.txt'), 'w', encoding='utf-8') as f:
        for label in labels:
            f.write(f"{label}\n")
    
    print('Done!')

split_bounding_boxes(info, 'original', 'image')
=======
from PIL import Image, ImageDraw
import cv2
import numpy as np
import os
from tqdm import tqdm
from convert import read_convert_label_file
from sklearn.model_selection import train_test_split

file_path = "/home/phuong/PaddleOCR/dataset/Data_Detec_Train/Augraphy_ColorPaper_Image/Label.txt"
info = read_convert_label_file(file_path)


def crop_img(info):
    data = []
    for i in info:
        for j in i[1]:
            data.append([i[0], j['transcription'], j['points']])
        break
    print(len(data))
    for img in data:
        coordinates = img
        print(coordinates)
        # coordinates = [tuple(sublist) for sublist in coordinates]
        # print(coordinates)

        # cropped_image = crop_polygon(info[219][0], coordinates)
        # cropped_image.show()

def crop_polygon(image, polygon_points):
    # image = Image.open(image_path)
    polygon_points = [tuple(sublist) for sublist in polygon_points]
    mask = Image.new('L', image.size, 0)
    ImageDraw.Draw(mask).polygon(polygon_points, outline=None, fill=255)
    
    cropped_image = Image.composite(image, Image.new('RGB', image.size, (255, 255, 255)), mask)
    cropped_image = cropped_image.crop(mask.getbbox())
    
    return cropped_image

def split_bounding_boxes(info, save_dir, label_name):

    os.makedirs(save_dir, exist_ok=True)
    img_sava_dir = os.path.join(save_dir, label_name)
    os.makedirs(img_sava_dir, exist_ok=True)

    count = 0
    labels = []
    for imgs in tqdm(info):
        img = Image.open(imgs[0])

        for label_bb in imgs[1]:
            label = label_bb['transcription']
            bb = label_bb['points']
            cropped_img = crop_polygon(img, bb)

            # Bỏ qua trường hợp 90% nội dung ảnh cắt là màu trắng hoặc đen.
            # if np.mean(cropped_img) < 35 or np.mean(cropped_img) > 220:
            #     continue

            # Bỏ qua trường hợp ảnh cắt có width < 10 hoặc heigh < 10
            # if cropped_img.size[0] < 10 or cropped_img.size[1] < 10:
            #     continue

            # Tạo tên cho file ảnh đã cắt và lưu vào save_dir
            filename = f"{count:06d}.jpg"
            cropped_img.save(os.path.join(img_sava_dir + '', filename))

            new_img_path = os.path.join(img_sava_dir, filename)

            # Đưa format label mới vào list labels
            # Format: img_path\tlabel
            label = new_img_path + '\t' + label

            labels.append(label)  # Append label to the list

            count += 1
        # break

    print(f"Created {count} images")

    # Đưa list labels vào file labels.txt
    with open(os.path.join(save_dir, 'rec_gt_'+label_name+'.txt'), 'w', encoding='utf-8') as f:
        for label in labels:
            f.write(f"{label}\n")
    
    print('Done!')

split_bounding_boxes(info, 'original', 'image')
>>>>>>> ddfcb7004e7c2ef5f5763c85de7b1cc2ce6b1345
# crop_img(info)