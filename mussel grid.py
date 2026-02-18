# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:30:16 2024

@author: aawad
"""

"""
#Please make sure the vertical axes of the images and labels matches
#the selected images have to correspond to the split in the original folder only and not necessarily to the splits of other models
#Please place the labels inside the 'labels' folder in the root directory. the labels must have the same vertical resolution as the images.
"""
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from combine_img import *
from generate_labels import generate_label

root_dir = r"D:\GLRC1000_Enhanced\GLRC1000\jpeg\Selected".replace('\\','/')
extension = r'png'
save_dir = r"C:\Users\aawad\Desktop"
#models = ["Original", "ACDC", "TEBCF", "AutoEnh", "ACCE_D", "HFM", "MMLE", "ROP", "SPDF", "UNTV", "WWPE"]
models = ["Original", "TUDA", "HFM", "MLLE"]
casts = ["Cast 1", "Cast 2", "Cast 3", "Cast 4", "Cast 5"]
selected = ['CI_1658159423_170', 'CI_1660338886_835', 'CI_1660435039_475', 'CI_1685907925_312', 'CI_1660328605_852']


title = []
for model in models:
    title.append(generate_label([model], label_size=(1920, 200), fontSize=200)[0])
titles = combine_images(columns=len(title), space=20, images=title)

filler = generate_label([""], label_size=(200, 200), fontSize=200)[0]
full_title = combine_images(columns=2, space=20, images=[filler, titles])

images=[]
#images.append(generate_label(
#    [""], label_size=(full_title.size[1], 200), fontSize=200, rotation=90)[0])
h = 1406
for image, cast in zip(selected, casts):
        images.append(generate_label([cast], label_size=(
            h, 200), fontSize=200, rotation=90)[0])
        for model in models:
            images.append(Image.open(f'{root_dir}/{model}/{image}.{extension}'))

        
images = combine_images(columns=len(models)+1, space=20, images = images)


figure = combine_images(columns=1, space=30, images=[full_title, images])


figure = np.asarray(figure)
plt.imsave(f'{save_dir}/Mussel.jpeg',
           figure, cmap=None, format='jpeg')
