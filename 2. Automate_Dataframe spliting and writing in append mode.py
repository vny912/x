import pandas as pd

df=pd.read_csv('test.csv')
a=df.shape[0]
s=100
for i in range(0,a,s):
    if i==0:
        temp=df[i:i+s]
        temp.to_csv('g.csv',mode='a',index=False)
    else:
        temp=df[i:i+s]
        temp.to_csv('g.csv',mode='a',index=False,header=False)
        
        
