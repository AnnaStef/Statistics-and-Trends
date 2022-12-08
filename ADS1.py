# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:41:00 2022

@author: shobi
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_1=pd.read_excel("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\fuel_import1.xlsx")
print(df_1)
#na_values=df_1.fillna(0)
df_2=df_1.iloc[[12,21,41,71,180],[0,53,54,55,56,57,58,59,60,61,62]]
df_2=df_2.set_axis(['Country','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False)
df_2.reset_index(drop=True, inplace=True)
print(df_2)
df_3=df_2.T
print(df_3)

plt.figure(dpi=144)
df_31=df_1.iloc[12,53:63]
df_32=df_1.iloc[21,53:63]
df_33=df_1.iloc[41,53:63]
df_34=df_1.iloc[71,53:63]
df_35=df_1.iloc[180,53:63]
plt.plot(df_31,label='UAE',dashes=[1,1])
plt.plot(df_32,label='Belgium',dashes=[2,2])
plt.plot(df_33,label='Switzerland',dashes=[3,3])
plt.plot(df_34,label='Egypt',dashes=[4,4])
plt.plot(df_35,label='Netherlands',dashes=[5,5])
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.show()

df_4=pd.read_excel("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\gdp.xlsx")
print(df_4)
#na_values=df_1.fillna(0)
df_5=df_4.iloc[[12,21,41,71,180],[0,53,54,55,56,57,58,59,60,61,62]]
df_5=df_5.set_axis(['Country','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False)
df_5.reset_index(drop=True, inplace=True)
print(df_5)
df_6=df_5.T
print(df_6)

plt.figure()
df_41=df_4.iloc[12,53:62]
df_42=df_4.iloc[21,53:62]
df_43=df_4.iloc[41,53:62]
df_44=df_4.iloc[71,53:62]
df_45=df_4.iloc[180,53:62]
plt.subplot(1,2,1)
plt.hist(df_41, label = "UAE",density = True)
plt.hist(df_42, label = "Belgium",alpha = 0.5)
plt.legend()
plt.subplot(1,2,2)
plt.hist(df_43, label = "Switzerland",density = True)
plt.hist(df_44, label = "Egypt",alpha = 0.5)
plt.legend()
plt.show()