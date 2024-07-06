# -*- coding: utf-8 -*-
"""
Program to calculate the CVs of mass and efficiency parameters per type and per cycle number

@author: alima
"""

## Importing essenial modules
import sys
sys.modules[__name__].__dict__.clear()

import pandas as pd
import numpy as np

### First round recovery amount and efficiency by filter type (Phase 2: Naturally loaded fiter)
df = pd.read_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary.xlsx')

df[['SN', 'Site_N', 'Round_N']] = df[['SN', 'Site_N', 'Round_N']].astype(str)

cv_list = ['M_d', 'M_d_cum', 'M_s', 'M_s_cum', 'M_t', 'M_t_cum', 'sCE', 
           'sCE_cum', 'tCE', 'tCE_cum', 'CE', 'CE_cum', 'M_C', 'M_C_cum']

a = df.groupby(['Cycle_N', 'ft'], as_index = False)['M_d', 'M_d_cum', 'M_s', 
                         'M_s_cum', 'M_t', 'M_t_cum', 'sCE', 'sCE_cum', 'tCE', 
                         'tCE_cum', 'CE', 'CE_cum', 'M_C', 'M_C_cum'].agg('std')

b = df.groupby(['Cycle_N', 'ft'], as_index = False)['M_d', 'M_d_cum', 'M_s', 
                         'M_s_cum', 'M_t', 'M_t_cum', 'sCE', 'sCE_cum', 'tCE', 
                         'tCE_cum', 'CE', 'CE_cum', 'M_C', 'M_C_cum'].mean()

df_cv = (a/b) * 100
df_cv.drop(['Cycle_N', 'ft'], axis = 1, inplace = True)

df_cv = pd.merge(a[['Cycle_N', 'ft']], df_cv[cv_list], left_index =True, right_index =True)

## Alternative method with numpy (different results from pandas aggregate. Explore why?)
df_cv_alt = df.groupby(['Cycle_N', 'ft'], as_index = False)['M_d', 'M_d_cum', 'M_s', 
                         'M_s_cum', 'M_t', 'M_t_cum', 'sCE', 'sCE_cum', 'tCE', 
                         'tCE_cum', 'CE', 'CE_cum', 'M_C', 'M_C_cum'].apply(lambda x: (np.std(x) / np.mean(x)) * 100)

