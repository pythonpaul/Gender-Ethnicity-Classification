import pandas as pd

from ethnicolr import *

import xlsxwriter
import sys
pd.options.display.float_format = '{:.0f}'.format
from ethnicolr import census_ln, pred_census_ln

def sakura_box():
    names = pd.read_csv('sakura_box_customer_analysis.csv')
    
    df = pred_census_ln(names, 'SHIPPING_LAST_NAME')
    print(df)
    df.to_excel('sakura_box_customer_ethn.xlsx')

sakura_box()
