# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:15:42 2024

@author: aawad
"""
from combine_img import *
from generate_labels import generate_label
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

images_path = r"C:\Users\aawad\Desktop\Detecction Enhancement Corrolation".replace('\\', '/')
extension = 'png'
datasets = ['RUOD', 'CUPDD'] #RUOD OR CUPDD
metrics = ['UIQM', 'UCIQE', 'CCF', 'Entropy']
save_dir = images_path

images = []
for dataset in datasets:
    for metric in metrics:
        images.append(Image.open(f"{images_path}/{dataset}-{metric}.{extension}"))
legend_image = Image.open(f"{images_path}/legend.{extension}")
legend_image = ImageOps.expand(legend_image, border=20, fill='gray')

w, h = images[0].size
legend_image.thumbnail((2.5*w, 300))

 
title_label = generate_label(["Detection-Enhancement Corrolation"], label_size = (2*w, 100), line = True)#, rotation = 90))
dataset_labels = generate_label(["CUPDD", "RUOD"], label_size = (h, 100), fontSize=50, rotation = 90)

pad = generate_label([""], label_size = (907, 75), fontSize=50)[0]
legend_image = get_concat_h(pad, legend_image)
legend_image = get_concat_h(legend_image, pad)


layer1 = combine_images(columns=1, space=0, images = dataset_labels)
layer2 = combine_images(columns=4, space=0, images = images)
figure = combine_images(columns=2, space=0, images = [layer1, layer2])#title_label[0]legend_image

figure = combine_images(columns=1, space=0, images = [figure, legend_image])#title_label[0]legend_image
figure = np.asarray(figure)
# Save without a cmap, to preserve the ones you saved earlier
plt.imsave(f'{save_dir}/corr.jpeg', figure,cmap=None, format='jpeg')
