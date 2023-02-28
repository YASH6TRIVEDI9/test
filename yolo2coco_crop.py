import cv2
import glob
import os
import random


for folder in glob.glob("/home/yash/Downloads/wbc_rbc/train/labels/*"):

    folder_name = os.path.basename(folder)
    print(folder_name)

    for txt_file in glob.glob(f"/home/yash/Downloads/wbc_rbc/train/labels/{folder_name}/*"):
        print(txt_file)

        txt_file_name = os.path.basename(txt_file)
        img_file_name = txt_file_name.replace(txt_file_name[-4:], ".jpg")
        img_file = f"/home/yash/Downloads/wbc_rbc/train/images/{folder_name}/{img_file_name}"

        img = cv2.imread(img_file)

        with open(txt_file) as file:

            lines = file.readlines()       # get lines from text file
                        
            cnt = 0
            for line in lines:             # get each line from lines
                rl = line.replace('  ', ' ')    # replace double space into single space in lines
                text = rl.split(" ") 


                classs = int(float(text[0]))
                x_yolo = float(text[1])
                y_yolo = float(text[2])
                width_yolo = float(text[3])
                height_yolo = float(text[4][:-1])

                width = img.shape[1]
                height = img.shape[0]

                h,w = abs(height_yolo*height),abs(width_yolo*width)
                x_coco = round(x_yolo*width -(w/2))
                y_coco = round(y_yolo*height -(h/2))
                if x_coco <0: #check if x_coco extends out of the image boundaries
                    x_coco = 1
                if y_coco <0: #check if y_coco extends out of the image boundaries
                    y_coco = 1

                if classs == 0:

                    crop_img = img[int(y_coco):int(y_coco + h), int(x_coco):int(x_coco + w)]

                    if not os.path.exists(f'/home/yash/Downloads/wbc_rbc/train/wbc_images/{folder_name}'):
                        os.makedirs(f'/home/yash/Downloads/wbc_rbc/train/wbc_images/{folder_name}')


                    cv2.imwrite(f'/home/yash/Downloads/wbc_rbc/train/wbc_images/{folder_name}/{img_file_name[:-4]}{cnt}.png',crop_img)
                    cnt += 1