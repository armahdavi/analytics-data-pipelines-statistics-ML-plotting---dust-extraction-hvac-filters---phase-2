# -*- coding: utf-8 -*-
"""
Program to make dataframes from all extraction lab data sheets (LDSs) from the naturally loaded filters

@author: alima
"""

## Essential modulees & files
import sys
sys.modules[__name__].__dict__.clear()

import pandas as pd


exec(open('C:/PhD Research/Generic Codes/notion_corrections.py').read())
exec(open('C:/PhD Research//Generic Codes/labels_all.py').read())

###################################################################
### Step 1: Loop for reading all LDSs and append to a master df ###
###################################################################

## Putting all excel files of LDSs in one list and operate on each file to extract essential information prior to appending
import os
orig_path = r'C:/PhD Research/Paper 1 - Extraction/Raw/natural_lds/'
os.chdir(orig_path)
list_dir = [x for x in os.listdir() if '18' in x]

## creating master df
import glob
df_append_all = pd.DataFrame([])

## looping over all LDS files and take important data
for dire in list_dir:
    os.chdir(orig_path + dire)
    file_list = glob.glob('lds_*.xlsx')
    for file in file_list:
        df = pd.read_excel(file, sheet_name = 'Extraction_data_entry', header=None)
        # taking all necessary constant values
        dust_mass = round(df.loc[2,3],3)
        SN = file[-25:-22]
        SiteN = file[-21:-19]
        RndN = file[-18:-16]
        filtertype = file[-15:-12]
        Exdate = file[-11:-5]
        
        # rereading with the rid of first 10 rows
        df = pd.read_excel(file, sheet_name = 'Extraction_data_entry', header=10)
        
        df['dustmass'] = dust_mass
        df['SN'] = int(SN)
        df['Site_N'] = int(SiteN) # this allows you to get rid of 0 prior to a digit; required for merging later
        df['Round_N'] = int(RndN)
        df['ft'] = filtertype
        df.replace({'ft':label_filter_type1}, inplace = True)  
               
        df['Mass_C'] = df['M_ph_full'] - df['M_ph_clean']
                
        varlist_drop = stata_varlist_split('Duration_min M_ph_clean M_ph_full M_ph_dumped M_vd M_vs Initials')
        # os.chdir(r'C:\Career\Learning\Python Practice\Generic Codes')
        df.drop(varlist_drop, axis = 1, inplace = True)
        
        df['M_C'] = df['M_C']*100
        df['M_C_cum'] = df['M_C_cum']*100
        
        df_append_all = df_append_all.append(df)


####################################################################
### Step 2: Refining, sorting and creating new important columns ###
####################################################################

df_append_all = df_append_all.drop(['M_vd_j', 'M_vs_j'], axis=1)
df_append_all.sort_values(['SN', 'Cycle_N'], inplace = True)

df_append_all['M_t'] = df_append_all['M_d'] + df_append_all['M_s']

df_append_all['M_t_cum'] = df_append_all['M_d_cum'] + df_append_all['M_s_cum']
df_append_all['sCE'] = (df_append_all['M_s'] / df_append_all['dustmass']) * 100
df_append_all['sCE_cum'] = (df_append_all['M_s_cum'] / df_append_all['dustmass']) * 100
df_append_all['tCE'] = ((df_append_all['M_d'] + df_append_all['M_s'])/df_append_all['dustmass']) * 100
df_append_all['tCE_cum'] = ((df_append_all['M_d_cum'] + df_append_all['M_s_cum'])/df_append_all['dustmass']) * 100

df_append_all['d_t_rat'] = df_append_all['M_d'] / df_append_all['M_t']
df_append_all['d_t_rat_cum'] = df_append_all['M_d_cum'] / df_append_all['M_t_cum']


new_order = ['SN', 'Site_N', 'Round_N', 'ft', 'Cycle_N', 'dustmass', 'M_filter_post', 
             'M_filter_change', 'M_filter_change_cum', 'M_d', 'M_d_cum', 'M_s', 'M_s_cum',
             'M_t', 'M_t_cum', 'sCE', 'sCE_cum', 'tCE', 'tCE_cum', 'E', 'E_cum', 'C', 'D', 
             'CE', 'CE_cum', 'M_C', 'M_C_cum', 'Mass_C', 'Label']

df_append_all = df_append_all[new_order]


##########################################
### Step 3: Merging, QA, and exporting ###
##########################################

## correction of negative process efficiencies
bad_data = df_append_all[ (df_append_all['E_cum']< 0) | (df_append_all['E_cum'] >100)]
bad_data = bad_data[['SN', "dustmass"]].groupby('SN', as_index = False)['dustmass'].agg('mean')
sn_list = list(bad_data['SN'].astype(int))

## Dust mass corrections
dustmass_correct = pd.read_stata('C:/PhD Research/Paper 1 - Extraction/Processed/natural/dataset_summary_complete_full_collapsed.dta')
dustmass_correct = dustmass_correct[['SN','dustmass']].astype(float).round(3)
dustmass_correct = dustmass_correct[dustmass_correct['SN'].isin(sn_list)]

df_append_all.to_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary.xlsx', index = False)

### collapsing all data to get max Cycl_N
varlist = stata_varlist_split('Cycle_N M_d_cum M_s_cum M_t_cum E_cum CE_cum sCE_cum tCE_cum dustmass ft Site_N Round_N M_filter_change_cum')

df_collapsed = df_append_all.groupby('SN', as_index = False)[varlist].agg('max')
m_c_collapsed = df_append_all.groupby('SN').apply(lambda x: x.iloc[-1:]).reset_index(drop=True)
m_c_collapsed = m_c_collapsed[['SN', 'M_C_cum']]
df_collapsed = df_collapsed.merge(m_c_collapsed, on = "SN", how = 'inner')

df_collapsed = df_collapsed[['SN', 'Site_N', 'Round_N', 'ft', 'Cycle_N', 'dustmass', 
                'M_filter_change_cum', 'M_d_cum', 'M_s_cum', 'M_t_cum', 'E_cum', 'CE_cum',
                'sCE_cum', 'tCE_cum', 'M_C_cum']]


## Merging runtimes into the collapsed data
runtime = pd.read_stata(backslash_correct(r'C:/PhD Research/Paper 1 - Extraction\Raw\runtime_summary.dta'))
runtime['id'] = runtime['site'].astype(str).apply(lambda x: x[:-2]) + '_' + runtime['filter_type'].astype(str).apply(lambda x: x[:-2])

runtime = runtime.groupby('id', as_index = False)['runtime'].mean()
runtime['Site_N']  = runtime['id'].str.split('_').apply(lambda x: x[0]).astype(int)
runtime['Round_N'] = runtime['id'].str.split('_').apply(lambda x: x[1]).astype(int)
del runtime['id']
runtime['runtime'] = runtime['runtime'].astype(float).round(decimals = 3)

df_collapsed = df_collapsed.merge(runtime, on = ['Site_N', 'Round_N'], how = 'left')
df_collapsed.to_excel('C:/PhD Research/Paper 1 - Extraction/Processed/natural/natl_dataset_summary_collapsed.xlsx', index = False)

