import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from pylab import rcParams

#reading CSV file and storing in a dataframe

df=pd.read_csv("D:\\Kaggle\\transactions-from-a-bakery\\BreadBasket_DMS.csv")

print(df.head(10))
print(list(df))

#Printing Item types
df.dtypes

#find mean , min, max 
print(df.describe())

# dropping any row if empty
#df.dropna()

#print Unique Item from above CSV file
print(df.Item.unique())

# Total number of items in Item column
#len(df.Item.unique())


# Groupby Item and applying Sum omn Transaction. Renaming column Item to Items and Transaction to Sum.

df1=df.groupby('Item', as_index=False)['Transaction'].sum().rename(columns={'Item':'Items','Transaction' : 'Sum'})

df2=df1.sort_values(by=['Sum'])
#df1.columns = df1.columns.droplevel(0)
print(df2)


#list((df.groupby('Item')['Transaction'].sum()))

df2=df1.head(10)

df3=df2.sort_values(by=['Sum'])
print(df3)


df4=df.loc[df['Item'] == 'Tea'] 

print(df4)



x=df3.Items
y=df3.Sum
plt.figure(figsize=(20, 15))
plt.scatter(x,y)
