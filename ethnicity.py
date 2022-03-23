import pandas as pd

from ethnicolr import *

import xlsxwriter
import sys
pd.options.display.float_format = '{:.0f}'.format
from ethnicolr import census_ln, pred_census_ln

def grocery():

    grocery_names = pd.read_excel('cleaned_customers2.xls')

    grocery_names['CUSTOMER_ID'] = grocery_names['CUSTOMER_ID'].astype('Int64').astype(str)

    print(grocery_names)

    #sys.exit()


    df = pred_census_ln(grocery_names, 'LAST_NAME')
    print(df)
    df.to_excel('ethnicity_analysis.xlsx')

def box():
    box_names = pd.read_csv('BOX_CUSTOMER_SNOWFLAKE.csv')
    print(box_names)

    #sys.exit()
    df = pred_census_ln(box_names, 'SHIPPING_LAST_NAME')
    print(df)
    df.to_excel('box_customer_ethn.xlsx')


def market():
    box_names = pd.read_csv('MARKET_CUSTOMER_SNOWFLAKE.csv')
    print(box_names)

    #sys.exit()
    df = pred_census_ln(box_names, 'SHIPPING_LAST_NAME')
    print(df)
    df.to_excel('market_customer_ethn.xlsx')

box()
market()