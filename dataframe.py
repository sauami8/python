import pandas as pd
import numpy as np

data1 = {"product1": ["computer","monitor","disk","mouse"], "price1": [150, 125,100,50]}

df1 = pd.DataFrame(data1)

print(df1.head())#, df1.info(), df1.shape

data2 = {"product2": ["computer","monitor","disk","mouse"], "price2": [125, 100,75,50]}

df2 = pd.DataFrame(data2)

print(df2)

df1['price2'] = df2['price2']
print(df1.head())

#new column in df

df1['price_match'] = np.where(df1['price1'] == df2['price2'], True, False)

print(df1.head())

df1['price_diff'] = np.where(df1['price1'] ==df2["price2"],0,df1['price1'] - df2['price2'])

print(df1.head())
