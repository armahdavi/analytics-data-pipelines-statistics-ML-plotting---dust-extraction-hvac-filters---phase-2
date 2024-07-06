# -*- coding: utf-8 -*-
"""
Program to create essential functions to read from processed recovery data from naturally loaded filters
The program has two functions:
    1) dr_catchert: which gives a threshold and retunrs detection rates per cucmulative extraction cycle
    2) Cycle_refine: which refine the unaggregated recovery dataframe to keep all the filters that has gone through n cycle of extraction (n is one of the inputs)

@author: alima
"""

import pandas as pd
exec(open('C:/PhD Research/Generic Codes/notion_corrections.py').read())



def dr_catcher(threshold):
    '''
    
    Parameters
    ----------
    threshold : TYPE
        DESCRIPTION.

    Returns
    -------
    sum_dr_data : TYPE
        DESCRIPTION.

    '''
    
    df = pd.read_excel(backslash_correct(r'C:\PhD Research\Paper 1 - Extraction\Processed\natural\natl_dataset_summary.xlsx'))
    tot = len(df['SN'].unique())

    thresh = threshold
    i = 1
    sum_dr_data = pd.DataFrame({'Cycle_N': [],
                                'Count_d': [],
                                'Count_t': [],
                                 'dr_d': [],
                                 'dr_t': []})

   ## calculates % or detection per cycles comparing to thresh
   while i <=6: # total # of cycles
        cut_df = df[df['Cycle_N'] <= i]
        cut_df = cut_df.groupby('SN', as_index = False)['Cycle_N', 'M_d_cum', 'M_t_cum'].agg('max')
        
        count_d = len(cut_df[cut_df['M_d_cum'] > thresh])
        count_t = len(cut_df[cut_df['M_t_cum'] > thresh])
        
        dr_d = round(((len(cut_df[cut_df['M_d_cum'] > thresh])/tot)) * 100)
        dr_t = round(((len(cut_df[cut_df['M_t_cum'] > thresh])/tot)) * 100)
        j = i - 1
        sum_dr_data.loc[j,'Cycle_N'] = i 
        sum_dr_data.loc[j, 'Count_d'] = count_d 
        sum_dr_data.loc[j, 'Count_t'] = count_t  
        sum_dr_data.loc[j, 'dr_d'] =  dr_d
        sum_dr_data.loc[j, 'dr_t'] = dr_t
        i += 1

    return sum_dr_data



def Cycle_Refine(df_input, n, cut = False):
    '''
    ## Two main inputs: 
        1- Name of dataframe to cut, 
        2- the cycle number to apply
    '''
    
    df = df_input
    cyc_list = list(df[df['Cycle_N'] == n]['SN'].unique())

    df = df[df['ExpN'].isin(cyc_list)]
    if cut:
        df = df[df['SN'] <= n]
    
    return df
    
