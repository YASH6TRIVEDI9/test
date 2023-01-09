import cv2
import glob
import os

i = 0
for txt_file in glob.glob("labelTxt/*"):
    
    file_name = os.path.basename(txt_file)
    file_name = file_name[:-4]
    image_file = file_name + ".png"
    image_file = os.path.join("images", image_file)
    img = cv2.imread(image_file)
    
    with open(txt_file) as file:
        lines = file.readlines()
        
        for line in lines:             # get each line from lines
            rl = line.replace('  ', ' ')    # replace double space into single space in lines
            text = rl.split(" ")            # split from space and get list of text 
    
            classs = float(text[0])
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

            rec = cv2.rectangle(img, (int(x_coco), int(y_coco)), (int(x_coco+w), int(y_coco+h)), (0,0,255), 5)

            cv2.imwrite(f"rec{i}.png", rec)
    i += 1
    if i == 5:
        break
