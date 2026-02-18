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

root_dir = r"R:\Gobby dataset\Selected".replace('\\','/')
extension = r'png'
save_dir = r"C:\Users\aawad\Desktop"
#models = ["Original", "ACDC", "TEBCF", "AutoEnh", "ACCE_D", "HFM", "MMLE", "ROP", "SPDF", "UNTV", "WWPE"]
models = ["Original", "Mask", "ACDC", "ACCE_D", "HFM", "MMLE"]
selected = ['image_raw_64302822 (2)', 'image_raw_64323724 (2)', 'image_raw_64943480 (2)']


title = []
title.append(generate_label(["Granule"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["Bedrock"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["Pebble"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["Gravelly"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["SlightlyGravelly"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["GravelMixes"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["Cobble"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["Boulder"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["Fine"], label_size=(1920, 200), fontSize=200)[0])
title.append(generate_label(["CoarseAlgae"], label_size=(1920, 200), fontSize=200)[0])
titles = combine_images(columns=len(title), space=20, images=title)

filler = generate_label([""], label_size=(200, 200), fontSize=200)[0]
full_title = combine_images(columns=2, space=20, images=[filler, titles])

images=[]
#images.append(generate_label(
#    [""], label_size=(full_title.size[1], 200), fontSize=200, rotation=90)[0])
for model in models:
    images.append(generate_label([model], label_size=(
        1020, 200), fontSize=130, rotation=90)[0])
    for image in selected:
        images.append(Image.open(f'{root_dir}/{model}/{image}.{extension}'))
        
images = combine_images(columns=4, space=20, images = images)


#figure = combine_images(columns=1, space=30, images=[full_title, images])


figure = np.asarray(images)
plt.imsave(f'{save_dir}/Goby.jpeg',
           figure, cmap=None, format='jpeg')
