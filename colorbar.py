# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:38:57 2024

@author: aawad
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import cmasher as cmr
import numpy as np
from PIL import Image


#plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

def colbar(size = (800*4+40, 300), cmap_name = 'gist_rainbow', cmap_range = (0.03, 0.4), ticks = np.arange(0,1.1,0.1), labelcolor = "#808080"):
    my_dpi = 92.60728755320785
    #path = r'C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\legend_Q.jpeg'
    w, h = size #without 'bbox tight', it would produce exactly the same resolution
    
    plt.ioff()
    fig, ax = plt.subplots(figsize=(w/my_dpi, h/my_dpi), dpi=my_dpi)
    
    l , u = cmap_range
    cmap = cmr.get_sub_cmap(cmap_name, l, u)
    cbar = mpl.colorbar.ColorbarBase(ax, cmap=cmap, orientation = 'horizontal',ticks=ticks) #extend='max'
    #cbar.set_label(label='Q-index', size=100, color="#808080", labelpad=-h/2, x=-0.1)#, loc= "left")
    cbar.ax.tick_params(labelsize=50, width=5, length=15,labelcolor=labelcolor, grid_color=labelcolor, color=labelcolor)
    plt.tight_layout(pad=1) #THIS IS WHERE THE REAL MAGIC HAPPENS!!!! SPENT ONE AND A HALF GLORIOUS DAYS FOR THIS ^_^
    #plt.axis('off')
    fig.canvas.draw()
    x = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
    
    
    return x
    #fig.savefig(path)#, bbox_inches = 'tight', pad_inches=[[0,0],[0.3,0]])#, pad_inches = 0.3)#dpi = 150 # pad_inches=[l, r, b, t])

#x = colbar()
#x.show()
"""
image = Image.open(path) 

  
right = math.floor((w-image.size[0])/2)
left = math.ceil((w-image.size[0])/2)
top = 0
bottom = 0
  
width, height = image.size 
  
new_width = width + right + left 
new_height = height + top + bottom 
  
result = Image.new(image.mode, (new_width, new_height), (255, 255, 255)) 
  
result.paste(image, (left, top)) 
  
result.save(path) 
"""