# -*- coding: utf-8 -*-
"""
Program to report log of extraction parameter values for statistical testing purposes

@author: alima
"""

## importing essential modules
import sys
sys.modules[__name__].__dict__.clear()

import pandas as pd
import numpy as np

df_append_all = pd.read_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary.xlsx')

## mass or efficiency parameters to be converted to logs
log_list = ['M_filter_change', 'M_filter_change_cum', 'M_d', 'M_d_cum', 'M_s',
            'M_s_cum', 'M_t', 'M_t_cum', 'sCE', 'sCE_cum', 'tCE', 'tCE_cum', 'E',
            'E_cum', 'C', 'D', 'CE', 'CE_cum', 'M_C', 'M_C_cum', 'Mass_C']

id_list = ['SN', 'Site_N', 'Round_N', 'ft', 'Cycle_N', 'dustmass']

df_append_all_log = df_append_all[id_list + log_list]

## log-making
for item in log_list:
    df_append_all_log[item] = np.log10(df_append_all[item])
    
