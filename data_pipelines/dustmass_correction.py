# -*- coding: utf-8 -*-
"""
Program to add corrected dust mass values from a Stata file

@author: alima
"""

## import essential files
import sys
sys.modules[__name__].__dict__.clear()
import pandas as pd


df_pandas = pd.read_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary_collapsed.xlsx')
df_stata = pd.read_stata('C:/PhD Research/Paper 1 - Extraction/Processed/natural/dataset_summary_complete_full_collapsed.dta')

## refining bad data
bad_data = df_pandas[ (df_pandas['E_cum']< 0) | (df_pandas['E_cum'] >100)]
bad_data = bad_data[['SN','dustmass']]
sn_list = list(bad_data['SN'])

dustmass_correct = pd.read_stata('C:/PhD Research/Paper 1 - Extraction/Processed/natural/dataset_summary_complete_full_collapsed.dta')
dustmass_correct = dustmass_correct[['SN','dustmass']].astype(float).round(3)

dustmass_correct = dustmass_correct[dustmass_correct['SN'].isin(sn_list)]

