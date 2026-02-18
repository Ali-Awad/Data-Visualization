# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:49:23 2024

@author: aawad
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#########################################################################################################
models = ["ACDC","TEBCF", "BayesRet", "PCDE", "ICSP", "AutoEnh", "Semi-UIR", "USUIR", "TUDA"]
CSV_dir = r"D:\GDrive\.shortcut-targets-by-id\1NPuVSs3jUSRcQJ0zW_RkdjmgsOtn3Nt_\Ali Awad\By Ali\Projects\IEEE Transaction - Image Processing\Figures\Metrics Calculated\UIF".replace('\\', '/')
Q_index_CSV_dir = r"D:\GDrive\.shortcut-targets-by-id\1NPuVSs3jUSRcQJ0zW_RkdjmgsOtn3Nt_\Ali Awad\By Ali\Projects\IEEE Transaction - Image Processing\Figures\Metrics Calculated".replace('\\', '/')
save_dir = r"D:\GDrive\.shortcut-targets-by-id\1NPuVSs3jUSRcQJ0zW_RkdjmgsOtn3Nt_\Ali Awad\By Ali\Projects\IEEE Transaction - Image Processing\Figures\Metrics Calculated\UIF".replace('\\', '/')
dataset = 'CUPDD' #RUOD OR CUPDD
metrics = ['UIF ↑']


for metric in metrics:
    df_metric = pd.DataFrame()
    df_Q = pd.DataFrame()
    for  model in models:
        df_UIF = pd.read_csv(f'{CSV_dir}/{dataset}/{model}.csv')
        df_Q_index = pd.read_csv(f'{Q_index_CSV_dir}/{dataset}/{model}.csv')
        df_metric[f'{model}'] = df_UIF[f'{metric}'.split(' ')[0]]
        df_Q[f'{model}'] = df_Q_index['Q-index ↑'.split(' ')[0]]
    #df_Q = df_Q.melt()
    df_Q['quartile'] = pd.cut(df_Q['value'], bins=4, labels=['Q1', 'Q2', 'Q2', 'Q3'])
    df_Q = df_Q.melt()
    df_metric = df_metric.melt()
    df_metric['quartile'] = df_Q['quartile']
    
    df_metric = df_metric.dropna()
    
    plt.ioff()
    f, ax = plt.subplots(figsize=(10, 11),linewidth=1, edgecolor="#bcbcbc")
    #f.f = plt.figure(linewidth=5, edgecolor="#04253a")

    # Show each distribution with both violins and points
    sns.barplot(data=df_metric, x= 'value', y='variable', hue = 'quartile', hue_order= ['Q1', 'Q2', 'Q3'],\
                   orient = 'h', palette=["#F3B664", "#F1EB90", "#9FBB73"])#"#EC8F5E",
    
    #sns.kdeplot(data=df_metric.melt(), x="value", hue="variable", alpha=.5, linewidth=4,) #palette="crest",fill=True, common_norm=False,
   
    #ax.legend_ = None
    
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

    