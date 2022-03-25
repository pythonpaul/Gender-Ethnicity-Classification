import gender_guesser.detector as gender
import pandas as pd

pd.options.display.float_format = '{:.0f}'.format

def grocery():

    grocery_names = pd.read_csv('jan_2022_data.csv')
    #grocery_names['SHIPPING_FIRST_NAME'] = grocery_names['SHIPPING_FIRST_NAME'].astype(str)

    d = gender.Detector()
    
    d.get_gender(grocery_names['SHIPPING_FIRST_NAME'][0])
    print(type(grocery_names['SHIPPING_FIRST_NAME'][0]))

    grocery_names['SHIPPING_FIRST_NAME'] = grocery_names['SHIPPING_FIRST_NAME'].str.lower().str.capitalize()
    grocery_names['gender'] = grocery_names['SHIPPING_FIRST_NAME'].apply(lambda x: d.get_gender(x))
    grocery_names['gender'] = grocery_names['gender'].apply(lambda x: x.replace('mostly_', ''))
    grocery_names['gender'] = grocery_names['gender'].apply(lambda x: x.replace('andy', 'Gender Neutral'))
    grocery_names['CUSTOMER_STATUS'] = grocery_names['CUSTOMER_STATUS'].apply(lambda x: x.replace('LAPSED_RETURNER', 'RETURNING'))
    #grocery_names['SHIPPING_FIRST_NAME'] = grocery_names['SHIPPING_FIRST_NAME'].apply(lambda x: x.replace(x, x.capitalize()))

    print(grocery_names)
    
    grocery_names.to_excel('jan_2022_data.xlsx')

grocery()