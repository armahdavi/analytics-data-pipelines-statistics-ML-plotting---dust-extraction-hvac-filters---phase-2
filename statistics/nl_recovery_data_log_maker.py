# -*- coding: utf-8 -*-
"""
Program to report log of extraction parameter values for statistical testing purposes

@author: alima
"""

### Essential modules
import sys
sys.modules[__name__].__dict__.clear()

import pandas as pd
import numpy as np


df = pd.read_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary.xlsx')
print(df.columns)

## parameters for log distribution
log_list = ['dustmass', 'M_filter_change', 'M_filter_change_cum', 'M_d', 'M_d_cum', 'M_s',
            'M_s_cum', 'M_t', 'M_t_cum', 'sCE', 'sCE_cum', 'tCE', 'tCE_cum', 'E',
            'E_cum', 'C', 'D', 'CE', 'CE_cum', 'M_C', 'M_C_cum', 'Mass_C']

## log-making
for var in log_list:
    df[var] = np.log10(df[var])
    
df.to_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary_log.xlsx', index = False)
