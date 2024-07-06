# -*- coding: utf-8 -*-
"""
calculating detection rates using dr_catcher function run from "natural_loading_functions.py

@author: alima
"""

import sys
sys.modules[__name__].__dict__.clear()

exec(open('C:/PhD Research/Paper 1 - Extraction/Code/natural/natural_loading_functions.py').read())


test = 6.9E-6 + 8.0E-5 + 5.7E-5

#### Worst
tm_wo_As = dr_catcher(0.00008)
tm_w_As = dr_catcher(0.07)
pcb = dr_catcher(0.44)


#### Medin
tm_wo_As = dr_catcher(0.00008)
tm_w_As = dr_catcher(0.07)
pcb = dr_catcher(0.07)


#### Best
tm_wo_As = dr_catcher(0.0000072)
tm_w_As = dr_catcher(0.003)
pcb = dr_catcher(0.001)


#### Constant
pah = dr_catcher(0.01)
pbde = dr_catcher(0.00034)
ph = dr_catcher(0.00056)


## The code does not work when you run it as a whole, but line by line
# error: name 'backslash_correct' is not defined
# error fixed if you take out exec command out of function

