# -*- coding: utf-8 -*-
"""
Created on Mon May 13 07:47:12 2024

@author: aawad
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#########################################################################################################
models = ["Original", "ACDC","TEBCF", "BayesRet", "PCDE", "ICSP", "AutoEnh", "Semi-UIR", "USUIR", "TUDA"]
CSV_dir = r"C:\Users\aawad\Desktop\IEEE Trans Sets\Q-index".replace('\\', '/')
save_dir = r"C:\Users\aawad\Desktop\IEEE Trans Sets\Q-index".replace('\\', '/')
dataset = 'RUOD' #RUOD OR CUPDD
metrics = ['UIQM ↑', 'UCIQE ↑', 'CCF ↑', 'Entropy ↑', 'Q-index ↑']
#metrics = ['UIQM ↑']

for metric in metrics:
    df_metric = pd.DataFrame()
    for  model in models:
        df_model = pd.read_csv(f'{CSV_dir}/{dataset}/{model}.csv')
        
        
        
        df_metric[f'{model}'] = df_model[f'{metric}'.split(' ')[0]]
        
    df_metric = df_metric.dropna()
    
    plt.ioff()
    f, ax = plt.subplots(figsize=(10, 11),linewidth=1, edgecolor="#bcbcbc")
    #f.f = plt.figure(linewidth=5, edgecolor="#04253a")

    # Show each distribution with both violins and points
    sns.violinplot(data=df_metric.melt(), x= 'value', y='variable', hue = True, inner="box",\
                   cut=2, linewidth=1, orient = 'v', split=True, palette='Paired', common_norm = 'True')
    
    #sns.kdeplot(data=df_metric.melt(), x="value", hue="variable", alpha=.5, linewidth=4,) #palette="crest",fill=True, common_norm=False,
   
    ax.legend_ = None
    
    sns.despine(left=True, top = False)
    
    #f.suptitle(f'{dataset}-Quality Distribution', fontsize=18, fontweight='bold')
    ax.set_title(f'{dataset}-Quality Distribution', fontsize=18, alpha=0.7)# fontweight='bold')
    ax.set(xlim=(0,1))
    ax.set_xticks(np.arange(0, 1.1, step=0.1)) 
    ax.set_ylabel("Models",size = 16,alpha=0.7)
    ax.set_xlabel(f"{metric}",size = 16,alpha=0.7)
    save_name = f'{save_dir}/{dataset}/{dataset}-{metric}.png'
    f.savefig(f'{save_name}', dpi = 150, bbox_inches = 'tight', pad_inches = 0.3)
    plt.close('all')
    