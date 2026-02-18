# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:56:45 2024

@author: aawad
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
#########################################################################################################
models = ["Original", "ACDC","TEBCF", "BayesRet", "PCDE", "ICSP", "AutoEnh", "Semi-UIR", "USUIR", "TUDA"]
#models = ["Original", "AutoEnh"]
mAP_CSV_dir = r"C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\reg".replace('\\', '/')
Qindex_CSV_dir = r'C:\Users\aawad\Desktop\IEEE Trans Sets\Q-index'.replace('\\', '/')
FP_dir = r'C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\rates'.replace('\\', '/')
Blur_dir = r'C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\reg\Blur'.replace('\\', '/')
UIQM_comp_dir = r'C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\reg\UIQM_comp'.replace('\\', '/')
save_dir = r"C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\FP plots".replace('\\', '/')
dataset = 'RUOD' #RUOD OR CUPDD
extracted_field_mAP = 'mAP' #mAP FP TP FN
extracted_field_Qindex = 'Q-index' #UIQM UCIQE CCF Entropy Q-index
index_field = 'images'
conf = 0.5
rnd = 2

df_metric = pd.DataFrame()
df_Q_all = pd.DataFrame()
df_UIQM = pd.DataFrame()
df_UCIQE = pd.DataFrame()
df_CCF = pd.DataFrame()
df_Entropy = pd.DataFrame()
df_fp = pd.DataFrame()
df_fn = pd.DataFrame()
df_tp = pd.DataFrame()
df_UICM = pd.DataFrame()
df_UIConM = pd.DataFrame()
df_UISM = pd.DataFrame()
df_Blur_Lap = pd.DataFrame()
df_Blur_SPIE = pd.DataFrame()


################### CHECK WHAT mAP CSV FILE YOU USE ⚠️##############################

for  model in models:
    df_model = pd.read_csv(f'{mAP_CSV_dir}/{dataset}_conf0.5_mAP50/{model}_mAP_conf{conf}.csv', dtype=str) #⚠️
    #df_model = pd.read_csv(f'{mAP_CSV_dir}/{dataset}_confBoth/{model}_mAP_conf{conf}.csv', dtype=str) #⚠️
    #df_model = pd.read_csv(f'{mAP_CSV_dir}/{dataset}_conf0.5_OrgCheckpoint/{model}_mAP.csv', dtype=str) #⚠️
    #df_model = pd.read_csv(f'{mAP_CSV_dir}/rates/{dataset}_conf0.1/{model}_rates.csv', dtype=str) #⚠️
    df_metric[f'{model}'] = df_model[f'{extracted_field_mAP}'.split(' ')[0]]
    df_Q = pd.read_csv(f'{Qindex_CSV_dir}/{dataset}/{model}.csv', index_col=0)
    df_Q_all[f'{model}'] = df_Q[f'{extracted_field_Qindex}'.split(' ')[0]].round(rnd)
    df_UIQM[f'{model}'] = df_Q['UIQM'.split(' ')[0]].round(rnd)
    df_UCIQE[f'{model}'] = df_Q['UCIQE'.split(' ')[0]].round(rnd)
    df_CCF[f'{model}'] = df_Q['CCF'.split(' ')[0]].round(rnd)
    df_Entropy[f'{model}'] = df_Q['Entropy'.split(' ')[0]].round(rnd)
    
    df_rates = pd.read_csv(f'{FP_dir}/{dataset}_Conf{conf}/{model}_rates.csv', index_col=0)
    df_fp[f'{model}'] = df_rates['FP']
    df_fn[f'{model}'] = df_rates['FN']
    df_tp[f'{model}'] = df_rates['TP']
    
    df_UIQM_comp = pd.read_csv(f'{UIQM_comp_dir}/{dataset}/{model}.csv', index_col=0)
    df_UICM[f'{model}'] = df_UIQM_comp['UICM']
    df_UIConM[f'{model}'] = df_UIQM_comp['UIConM']
    df_UISM[f'{model}'] = df_UIQM_comp['UISM']
    
    
    df_Blur = pd.read_csv(f'{Blur_dir}/{dataset}/{model}_Blur.csv', index_col=0)
    df_Blur_Lap[f'{model}'] = df_Blur['Blur_Lap']
    df_Blur_SPIE[f'{model}'] = df_Blur['Blur_SPIE']
    
##################################################################################################################
#post processing to add the index field with the propoer prefix and convert other columns to the right data type
#because I saved those CSV wrong
fix_index = True
if fix_index:
    df_metric[index_field] = df_model[index_field]
    df_metric[index_field] = df_metric[index_field] + '.jpg'
    df_metric.set_index(index_field, inplace=True)
    df_metric = df_metric.astype(float)
###################################################################################################################
df_metric = df_metric.round(rnd)
df_Q_all.reindex(df_metric.index)
df_UIQM.reindex(df_metric.index)
df_UCIQE.reindex(df_metric.index)
df_CCF.reindex(df_metric.index)
df_Entropy.reindex(df_metric.index)
df_fp.reindex(df_metric.index)
df_fn.reindex(df_metric.index)
df_tp.reindex(df_metric.index)
df_UICM.reindex(df_metric.index)
df_UIConM.reindex(df_metric.index)
df_UISM.reindex(df_metric.index)
df_Blur_Lap.reindex(df_metric.index)
df_Blur_SPIE.reindex(df_metric.index)

#get the Q-index indecies that match the indecies in the mAP dataframe
df_Q_all = df_Q_all[df_Q_all.index.isin(df_metric.index)]
df_UIQM = df_UIQM[df_UIQM.index.isin(df_metric.index)]
df_UCIQE = df_UCIQE[df_UCIQE.index.isin(df_metric.index)]
df_CCF = df_CCF[df_CCF.index.isin(df_metric.index)]
df_Entropy = df_Entropy[df_Entropy.index.isin(df_metric.index)]
df_fp = df_fp[df_fp.index.isin(df_metric.index)]
df_fn = df_fn[df_fn.index.isin(df_metric.index)]
df_tp = df_tp[df_tp.index.isin(df_metric.index)] 
df_UICM = df_UICM[df_UICM.index.isin(df_metric.index)]
df_UIConM = df_UIConM[df_UIConM.index.isin(df_metric.index)]
df_UISM = df_UISM[df_UISM.index.isin(df_metric.index)]
df_Blur_Lap = df_Blur_Lap[df_Blur_Lap.index.isin(df_metric.index)]
df_Blur_SPIE = df_Blur_SPIE[df_Blur_SPIE.index.isin(df_metric.index)]

#df_Q_sub = df_Q_all

change = True # whether to calculate the chnage in the mAP or the absolute mAP
if change:
    models.remove("Original")
    df_metric = df_metric.sub(df_metric['Original'], axis=0)
    df_Q_all = df_Q_all.sub(df_Q_all['Original'], axis=0)
    df_UIQM = df_UIQM.sub(df_UIQM['Original'], axis=0)
    df_UCIQE = df_UCIQE.sub(df_UCIQE['Original'], axis=0)
    df_CCF = df_CCF.sub(df_CCF['Original'], axis=0)
    df_Entropy = df_Entropy.sub(df_Entropy['Original'], axis=0)
    df_fp = df_fp.sub(df_fp['Original'], axis=0)
    df_fn = df_fn.sub(df_fn['Original'], axis=0)
    df_tp = df_tp.sub(df_tp['Original'], axis=0)
    df_UICM = df_UICM.sub(df_UICM['Original'], axis=0)
    df_UIConM = df_UIConM.sub(df_UIConM['Original'], axis=0)
    df_UISM = df_UISM.sub(df_UISM['Original'], axis=0)
    df_Blur_Lap = df_Blur_Lap.sub(df_Blur_Lap['Original'], axis=0)
    df_Blur_SPIE = df_Blur_SPIE.sub(df_Blur_SPIE['Original'], axis=0)


filterOutLiers = False
if filterOutLiers:
    df_metric = df_metric[(np.abs(stats.zscore(df_metric)) < 3).all(axis=1)]
    df_Q_all = df_Q_all[(np.abs(stats.zscore(df_Q_all)) < 3).all(axis=1)]

if change:
    metrics_names = ['Subset size', '∆ UIQM','∆ UCIQE', '∆ CCF','∆ UICM', '∆ UIConM', '∆ UISM', '∆ Entropy','∆ Blur_SPIE', '∆ TP','∆ FP', '∆ FN', '∆ mAP']
else:
    metrics_names = ['Subset size', 'UIQM', 'UCIQE', 'CCF', 'UICM', 'UIConM', 'UISM', 'Entropy', 'Blur_SPIE', 'TP', 'FP', 'FN', 'mAP']

df_everything = pd.DataFrame(columns = metrics_names)
df_overlapp_ge = pd.DataFrame(np.nan, index=range(4200), columns = models)
df_overlapp_lesser = pd.DataFrame(np.nan, index=range(4200), columns = models)
df_overlapp_ge = pd.DataFrame()
df_overlapp_lesser = pd.DataFrame()
for model in models:
    if change:
        df_metric_sub = df_metric
    else:
        df_metric_sub = df_metric.sub(df_metric['Original'], axis=0)
    df_greater = df_metric_sub[[f'{model}']].ge(0)
    df_greater = df_greater[df_greater[f"{model}"]==True]
    df_lesser = df_metric_sub[[f'{model}']].lt(0)
    df_lesser = df_lesser[df_lesser[f"{model}"]==True]
    gt_cent = int(round((len(df_greater)/len(df_metric)), rnd) * 100)
    lt_cent = int(round((len(df_lesser)/len(df_metric)), rnd) * 100)
    

    
    df_overlapp_ge = pd.concat([df_overlapp_ge,df_greater.index.to_frame()],axis=1)
    df_overlapp_lesser = pd.concat([df_overlapp_lesser,df_lesser.index.to_frame()],axis=1)
    r"""
    df_overlapp_ge = df_overlapp_ge.set_axis(models, axis=1)
    df_overlapp_lesser = df_overlapp_lesser.set_axis(models, axis=1)
    df_overlapp_ge.to_csv(r'C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\reg\overlap\images_ge_mAP50.csv', index=False)
    df_overlapp_lesser.to_csv(r'C:\Users\aawad\Desktop\Detecction Enhancement Corrolation\reg\overlap\images_lesser_mAP50.csv', index=False)
    """
    pd_row = []
    if model != 'Original': #grater is or lesser is not applicable for the Original images
        pd_row.append(f'{gt_cent}%')
        
        pd_row.append(df_UIQM[f'{model}'][df_UIQM[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_UCIQE[f'{model}'][df_UCIQE[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_CCF[f'{model}'][df_CCF[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        
        pd_row.append(df_UICM[f'{model}'][df_UICM[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_UIConM[f'{model}'][df_UIConM[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_UISM[f'{model}'][df_UISM[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_Entropy[f'{model}'][df_Entropy[f'{model}'].index.isin(df_greater.index)].std().round(rnd))    
        pd_row.append(df_Blur_SPIE[f'{model}'][df_Blur_SPIE[f'{model}'].index.isin(df_greater.index)].std().round(rnd))

        #pd_row.append(df_Q_all[f'{model}'][df_Q_all[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        #pd_row.append(df_Blur_Lap[f'{model}'][df_Blur_Lap[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        
        pd_row.append(df_fp[f'{model}'][df_fp[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_fn[f'{model}'][df_fn[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_tp[f'{model}'][df_tp[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        pd_row.append(df_metric[f'{model}'][df_metric[f'{model}'].index.isin(df_greater.index)] .std().round(rnd))
        
        df_everything.loc[f'mAP({model}) ≥ mAP(Org)'] = pd_row
        pd_row = []
    

    #if model == 'Original':
        #df_everything.loc['Total Original'] = pd_row

        
    if model != 'Original':
        pd_row.append(f'{lt_cent}%')
        
        pd_row.append(df_UIQM[f'{model}'][df_UIQM[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_UCIQE[f'{model}'][df_UCIQE[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_CCF[f'{model}'][df_CCF[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        
        pd_row.append(df_UICM[f'{model}'][df_UICM[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_UIConM[f'{model}'][df_UIConM[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_UISM[f'{model}'][df_UISM[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_Entropy[f'{model}'][df_Entropy[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))    
        pd_row.append(df_Blur_SPIE[f'{model}'][df_Blur_SPIE[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        
        #pd_row.append(df_Q_all[f'{model}'][df_Q_all[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        #pd_row.append(df_Blur_Lap[f'{model}'][df_Blur_Lap[f'{model}'].index.isin(df_greater.index)].std().round(rnd))
        
        pd_row.append(df_fp[f'{model}'][df_fp[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_fn[f'{model}'][df_fn[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_tp[f'{model}'][df_tp[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        pd_row.append(df_metric[f'{model}'][df_metric[f'{model}'].index.isin(df_lesser.index)].std().round(rnd))
        
        df_everything.loc[f'mAP({model}) < mAP(Org)'] = pd_row
        
        #df_everything.loc[f'Total {model}'] = ((df_everything.loc[f'mAP({model}) > mAP(Org) [{gt_cent}%]'] * gt_cent + df_everything.loc[f'mAP({model}) = mAP(Org) [{eq_cent}%]'] * eq_cent + df_everything.loc[f'mAP({model}) < mAP(Org) [{lt_cent}%]'] * lt_cent)/100).round(rnd)

########################################################################################


