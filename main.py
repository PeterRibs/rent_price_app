import pandas as pd

data2 = pd.read_csv("houses_to_rent_v2.csv")

data2.head()

data2.describe()

data2.city.unique()

data2.animal.unique()

data2.furniture.unique()

data3=None

data3.animal=data2.animal.replace('acept', True)

data3.animal=data3.animal.replace('not acept', False)

data3.furniture=data3.furniture.replace('furnished', True)

data3.furniture=data3.furniture.replace('not furnished', False)

data3.animal.unique()

data3.furniture.unique()

data3.head()

data3.columns

data3 = data3.rename(columns={'parking spaces':'parking_spaces','hoa (R$)':'hoa', 'rent amount (R$)':'rent_amount', 'property tax (R$)':'property_tax', 'fire insurance (R$)':'fire_insurance', 'total (R$)':'total'})

data3.head()