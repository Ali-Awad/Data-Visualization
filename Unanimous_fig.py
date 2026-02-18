# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:04:43 2024

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

root_dir = r"C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\reg\overlap\inference_Dataset".replace('\\','/')
extension = r'*.jpg.jpg'
save_dir = r"C:\Users\aawad\Desktop"
models = ["Original", "ACDC", "TEBCF", "BayesRet", "PCDE",
          "ICSP", "AutoEnh", "Semi-UIR", "USUIR", "TUDA"]
selected = ['000082.jpg.jpg', '004498.jpg.jpg', '013133.jpg.jpg', '000048.jpg.jpg', '003275.jpg.jpg', '004443.jpg.jpg']

title_1 = []
title_1.append(generate_label(["Enh > Org"], label_size=(800*2+20, 200), fontSize=120)[0])
title_1.append(generate_label(
    ["--------------------------------"], label_size=(200, 100), fontSize=100, offset=-20, rotation=90)[0])
title_1.append(generate_label(["Enh = Org"], label_size=(800*2+20, 200), fontSize=120)[0])
title_1.append(generate_label(
    ["--------------------------------"], label_size=(200, 100), fontSize=100, offset=-20, rotation=90)[0])
title_1.append(generate_label(["Enh < Org"], label_size=(800*2+20, 200), fontSize=120)[0])
titles_1 = combine_images(columns=len(title_1), space=20, images=title_1)

title = []
title.append(generate_label(["Sample #1"], label_size=(800, 200), fontSize=100)[0])
title.append(generate_label(["Sample #2"], label_size=(800, 200), fontSize=100)[0])
title.append(generate_label(
    ["--------------------------------"], label_size=(200, 100), fontSize=100, offset=-20, rotation=90)[0])
title.append(generate_label(["Sample #1"], label_size=(800, 200), fontSize=100)[0])
title.append(generate_label(["Sample #2"], label_size=(800, 200), fontSize=100)[0])
title.append(generate_label(
    ["--------------------------------"], label_size=(200, 100), fontSize=100, offset=-20, rotation=90)[0])
title.append(generate_label(["Sample #1"], label_size=(800, 200), fontSize=100)[0])
title.append(generate_label(["Sample #2"], label_size=(800, 200), fontSize=100)[0])
titles_2 = combine_images(columns=len(title), space=20, images=title)



full_title = combine_images(columns=1, space=20, images=[titles_1, titles_2])

filler = generate_label([""], label_size=(200, full_title.size[1]), fontSize=100)[0]
full_title = combine_images(columns=2, space=20, images=[filler, full_title])

#images.append(generate_label([selected.loc[image]["Model"]], label_size=(
#    600, 200), fontSize=90, rotation=90)[0])


#title.append(generate_label(
#    [""], label_size=(100, 200), fontSize=100)[0])


count = 1
images=[]
#images.append(generate_label(
#    [""], label_size=(full_title.size[1], 200), fontSize=100, rotation=90)[0])
for model in models:
    count = 1
    images.append(generate_label([model], label_size=(
        600, 200), fontSize=90, rotation=90)[0])
    for image in selected:
        images.append(Image.open(f'{root_dir}/{model}/{image}'))
        if (count % 2 == 0) and count != 0 and count<6:
            images.append(generate_label(
                ["--------------------------------"], label_size=(600, 100), fontSize=100, offset=-20, rotation=90)[0])
        count = count + 1
        
images = combine_images(columns=9, space=20, images = images)


figure = combine_images(columns=1, space=30, images=[full_title, images])


figure = np.asarray(figure)
plt.imsave(f'{save_dir}/unani.jpeg',
           figure, cmap=None, format='jpeg')
