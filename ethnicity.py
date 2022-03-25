import pandas as pd

from ethnicolr import *


pd.options.display.float_format = '{:.0f}'.format
from ethnicolr import census_ln, pred_census_ln

def sakura_box():
    names = pd.read_csv('jan_2022_data.csv')
    df = pred_census_ln(names, 'SHIPPING_LAST_NAME')
    
    print(df)
    df.to_excel('jan_2022_data.xlsx')

sakura_box()
