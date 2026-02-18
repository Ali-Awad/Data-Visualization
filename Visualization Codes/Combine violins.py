# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:17:49 2024

@author: aawad
"""
from combine_img import *
from generate_labels import generate_label
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

root_dir = r"C:\Users\aawad\Desktop\IEEE Trans Sets\Q-index".replace('\\', '/')
dataset = "CUPDD"
images = []

images.append(Image.open(rf"{root_dir}/{dataset}/1.png"))
w , h = images[0].size
images.append(generate_label(
    ["--------------------------------------------------------"], label_size=(h, 100), fontSize=50, offset=0, rotation=90)[0])
images.append(Image.open(rf"{root_dir}/{dataset}/2.png"))



images.append(Image.open(rf"{root_dir}/{dataset}/3.png"))

figure = combine_images(columns=len(images), space=1, images=images)
figure = np.asarray(figure)
plt.imsave(f"{root_dir}/{dataset}.jpeg", figure, cmap=None, format='jpeg')