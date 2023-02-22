import json
import urllib
import os 
from PIL import Image 
import glob
import cv2
from pathlib import Path

import os
from random import choice
import shutil
import torch


classes = {
'wall_ext_unhackable': 0,
'wall_int_unhackablewall': 1,
 'wall_hackable': 2,
 'wall_baywindow':3,
 'door_entrance': 4,
 'door_slidingdoor': 5,
 'door_maindoor': 6,
 'door_swingdoor': 7,
 'door_bifolddoor': 8,
 'window_tophungwindow': 9,
 'window_slidingwindow': 10,
 'window_casementwindow': 11,
 'furniture': 12,
 'wardrobe': 13,
  '2_seatersofa': 14,
 'toiletbowl': 15,
 'kitchen_cabinet': 16,
 'wall_pillar': 17,
 'db_eletricalbox': 18,
 'window_railing': 19,
 '2headerbed': 20,
  'diningtable': 21,
  '3_seatersofa': 22,
  '1headerbed': 23,
  '1_seatersofa': 24,
  'sink': 25,
  'toilet_basin': 26,
}


class CocoToYolo:

    def __init__(self, path, save_dir_name, classes):
        self.path = path
        self.classes = classes
        # if folder is not there then it will create one.
        if not os.path.exists(save_dir_name):
            os.mkdir(save_dir_name)
        self.save = save_dir_name

    def json_read(self):
        data = json.load(self.path)
    #     return data
    # def cnv(self, data):
        total_available_classes = []
        for image_id in range(len(data)):
            image_link = data[image_id]['Labeled Data']
            print(data[image_id]['External ID'])
            try:
                im = urllib.request.urlretrieve(image_link, f"/home/yash/Desktop/yolo_data_freefuse/yolo_title_large/{self.save}/" + str(data[image_id]['External ID']))
                image_url = data[image_id]["Labeled Data"]
                filename = f"/home/yash/Desktop/yolo_data_freefuse/yolo_title_large/{self.save}/" + str(data[image_id]['External ID'])
                print(filename)
                img = cv2.imread(filename)
                h_img, w_img = img.shape[:2]
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                for j in range(len(data[image_id]['Label']['objects'])):
                    if data[image_id]['Label']['objects'][j]["value"] not in total_available_classes:
                        total_available_classes.append(data[image_id]['Label']['objects'][j]["value"])
                    line = data[image_id]['Label']['objects'][j]
                    if 'bbox' in line:
                        bbox = data[image_id]['Label']['objects'][j]["bbox"]
                        x = (bbox['left'] + (bbox['width'] // 2)) / w_img
                        y = (bbox['top'] + (bbox['height'] // 2)) / h_img
                        w = bbox['width'] / w_img
                        h = bbox['height'] / h_img
                        print(classes[data[image_id]['Label']['objects'][j]["value"]], x, y, w, h)
                        file = open(f"/home/yash/Desktop/yolo_data_freefuse/yolo_title_large/{self.save}/" + str(data[image_id]['External ID'].split('.')[0]) + ".txt", 'a')
                        file.write(
                            "%s %s  %s  %s  %s" % (classes[data[image_id]['Label']['objects'][j]["value"]], x, y, w, h) + "\n")
                    else:
                        pass
            except Exception as e:
                print("************************************************")
                print((data[image_id]['External ID'],e))


    def jpg_to_png(self):
        directory = f"/home/yash/Desktop/coding/{self.save}/"

        os.chdir(f"/home/yash/Desktop/coding/{self.save}/")

        cwd = os.getcwd()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(cwd)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


        for filename in os.listdir(directory):
            if filename.endswith(".jpg"):
                print(filename)
                prefix = filename.split(".jpg")[0]
                os.rename(os.path.join(f"/home/yash/Desktop/coding/{self.save}/",filename), prefix+".png")
            if filename.endswith(".jpeg"):
                prefix = filename.split(".jpeg")[0]
                print(prefix)
                os.rename(os.path.join(f"/home/yash/Desktop/coding/{self.save}/",filename), prefix+".png")
            if filename.endswith(".gif"):
                # prefix = filename.split(".gif")[0]
                # print(prefix)
                # os.rename(os.path.join("/home/yash/Desktop/coding/yolo_img9/",filename), prefix+".png")
                os.remove(os.path.join(f"/home/yash/Desktop/coding/{self.save}/",filename))
            else:
                continue
            
        # print("$$$$$")
        print(cwd)
            
    # Delete file which doesn't have text file.

    def delelte_not_textfile(self):
        directory = f"/home/yash/Desktop/coding/{self.save}/"
        for filename in os.listdir(directory):
            if filename.endswith(".png"):
                prefix = filename.split(".png")[0] 
                if (os.path.exists(f"/home/yash/Desktop/coding/{self.save}/{prefix}.txt") == False):
                    os.remove(os.path.join(f"/home/yash/Desktop/coding/{self.save}/{filename}"))