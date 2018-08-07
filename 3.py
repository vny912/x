import timeit

start = timeit.default_timer()

import pandas as pd
import csv

for _ in range(1000):
    df=pd.read_csv('train.csv',chunksize=100)
    df1=tuple(df)

    for i in range(len(df1)):
        j=df1[i].to_dict('records')


stop = timeit.default_timer()

print (stop - start)

