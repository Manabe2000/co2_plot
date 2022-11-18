import math
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
import datetime as dt

mg = 500
k = 20
v_e = 870
v_0 = 333

v_list = []
v_2list = []
t_list = []

df = pd.read_csv('feeds.csv', index_col=1)
df['created_at'] = pd.to_datetime(df['created_at'])
# df1 = df[(df['created_at'] > pd.to_datetime("2022-08-31T10:00:00+09:00")) & (df['created_at'] < pd.to_datetime("2022-09-01T21:00:00+09:00"))]

fig,ax = plt.subplots()

for t in range(0,400):
    v_2 = df.at[88331 + t,'field1']
    t = t / 1000
    v = (mg/k)*(1 - math.exp((-k)*t)) + v_e*(1 - math.exp((-k)*t)) + v_0*(math.exp((-k)*t))
    v_list.append(v)
    v_2list.append(v_2)
    t_list.append(t)

ax.plot(t_list,v_list)
ax.plot(t_list,v_2list)
 
plt.show()
