import gender_guesser.detector as gender
import pandas as pd

pd.options.display.float_format = '{:.0f}'.format

def grocery():

    grocery_names = pd.read_excel('cleaned_customers2.xls')
    grocery_names['CUSTOMER_ID'] = grocery_names['CUSTOMER_ID'].astype('Int64').astype(str)

    d = gender.Detector()

    print(len(grocery_names['FIRST_NAME']))
    x = len(grocery_names['FIRST_NAME'])
    grocery_names['FIRST_NAME'] = grocery_names['FIRST_NAME'].str.lower().str.capitalize()
    grocery_names['gender'] = grocery_names['FIRST_NAME'].apply(lambda x: d.get_gender(x))

    print(grocery_names)
    grocery_names.to_excel('gender_analysis.xlsx')

def box():
    grocery_names = pd.read_csv('BOX_CUSTOMER_SNOWFLAKE.csv')
    grocery_names['CUSTOMER_ID'] = grocery_names['CUSTOMER_ID'].astype('Int64').astype(str)

    d = gender.Detector()

    print(len(grocery_names['SHIPPING_FIRST_NAME']))
    x = len(grocery_names['SHIPPING_FIRST_NAME'])
    grocery_names['SHIPPING_FIRST_NAME'] = grocery_names['SHIPPING_FIRST_NAME'].str.lower().str.capitalize()
    grocery_names['gender'] = grocery_names['SHIPPING_FIRST_NAME'].apply(lambda x: d.get_gender(x))
    grocery_names['gender'] = grocery_names['gender'].apply(lambda x: x.replace('mostly_', ''))

    print(grocery_names)
    grocery_names.to_excel('box_gender_analysis.xlsx')


box()

def market():
    grocery_names = pd.read_csv('MARKET_CUSTOMER_SNOWFLAKE.csv')
    grocery_names['CUSTOMER_ID'] = grocery_names['CUSTOMER_ID'].astype('Int64').astype(str)

    d = gender.Detector()

    print(len(grocery_names['SHIPPING_FIRST_NAME']))
    x = len(grocery_names['SHIPPING_FIRST_NAME'])
    grocery_names['SHIPPING_FIRST_NAME'] = grocery_names['SHIPPING_FIRST_NAME'].str.lower().str.capitalize()
    grocery_names['gender'] = grocery_names['SHIPPING_FIRST_NAME'].apply(lambda x: d.get_gender(x))
    grocery_names['gender'] = grocery_names['gender'].apply(lambda x: x.replace('mostly_', ''))

    print(grocery_names)
    grocery_names.to_excel('market_gender_analysis.xlsx')


market()


#for i in range(x):
#    print(d.get_gender(grocery_names['FIRST_NAME'][i]))

#print(d.get_gender(u"Kelly"))
#print(d.get_gender())



