import pandas as pd

from ethnicolr import *


pd.options.display.float_format = '{:.0f}'.format
from ethnicolr import census_ln, pred_census_ln

def sakura_box():
    names = pd.read_csv('feb_2022_data.csv')
    df = pred_census_ln(names, 'SHIPPING_LAST_NAME')
    df['CUSTOMER_STATUS'] = df['CUSTOMER_STATUS'].apply(lambda x: x.replace('LAPSED_RETURNER', 'RETURNING'))

    #     grocery_names['gender'] = grocery_names['gender'].apply(lambda x: x.replace('mostly_', ''))

    print(df)
    df.to_excel('feb_2022_ethnicity.xlsx')

sakura_box()
