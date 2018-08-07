import pandas as pd

df=pd.read_csv('test.csv')

#creating a dataframe from 0 to 99 rows then writing it to a csv
df1=df[:100]
df1.to_csv('b.csv',mode='a',index=False)

#creating a new dataframe from 101 to 200 rows writing it in same csv
df2=df[100:200]
df2.to_csv('b.csv',mode='a',index=False,header=False)
