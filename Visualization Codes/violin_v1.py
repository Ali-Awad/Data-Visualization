# -*- coding: utf-8 -*-
"""
Created on Mon May 13 07:47:12 2024

@author: aawad
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#########################################################################################################
models = ["Original", "ACDC","TEBCF", "BayesRet", "PCDE", "ICSP", "AutoEnh", "Semi-UIR", "USUIR", "TUDA"]
project_dir =  r"D:\GDrive\.shortcut-targets-by-id\1NPuVSs3jUSRcQJ0zW_RkdjmgsOtn3Nt_\Ali Awad\By Ali\Projects".replace('\\', '/')
CSV_dir = r"C:\Users\aawad\Desktop\IEEE Trans Sets\Q-index".replace('\\', '/')
save_dir = r"C:\Users\aawad\Desktop\IEEE Trans Sets\Q-index".replace('\\', '/')
dataset = 'CUPDD' #RUOD OR CUPDD
#metrics = ['UIQM ↑', 'UCIQE ↑', 'CCF ↑', 'Entropy ↑', 'Q-index ↑']
metrics = ['Q-index ↑']

for metric in metrics:
    df_metric = pd.DataFrame()
    for  model in models:
        df_model = pd.read_csv(f'{CSV_dir}/{dataset}/{model}.csv')
        df_metric[f'{model}'] = df_model[f'{metric}'.split(' ')[0]]
        
########################################################################################### 
#Subtracted Q-index       
    df_metric_sub = df_metric.sub(df_metric['Original'], axis=0)  
    df_metric_sub['Original'] = df_metric['Original']
    #df_metric_sub = df_metric_sub.drop("Original", axis=1)
    #df_metric_Org = pd.DataFrame()
    #df_metric_Org['Original'] = df_metric['Original']
    #df_melted_Org = df_metric_Org.melt()
###########################################################################################   
 
    df_metric_sub = df_metric_sub.dropna()
    df_melted = df_metric_sub.melt()
    
    #plt.ioff()
    f, ax = plt.subplots(figsize=(12, 8))
    sns.set(style="ticks")
    sns.set_style("whitegrid")
    # Show each distribution with both violins and points
    sns.violinplot(data=df_melted, x='variable', y = 'value', hue='variable', inner="box", palette="Set3", cut=2, linewidth=1)
    
    #sns.despine(top=True, bottom = True)
    
    f.suptitle(f'{dataset}-Quality Distribution', fontsize=18, alpha=0.7)
    plt.subplots_adjust(top=0.92)
    sns.set_style("whitegrid")
    ax.set_xlabel("Models",size = 16,alpha=0.7)
    ax.set_ylabel(f"Δ of {metric}",size = 16,alpha=0.7)
    #ax.set_ylabel(f"{metric}",size = 16,alpha=0.7)
    ax.set(ylim=(-0.6,1))
    save_name = f'{save_dir}/{dataset}/{dataset}-{metric}.png'
    f.savefig(f'{save_name}', dpi = 150, bbox_inches = 'tight')#, pad_inches = 0.3)
    plt.close('all')
    