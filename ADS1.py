import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Read_data1(file_name1):
    data1=pd.read_excel(file_name1)
    data1=data1.iloc[[12,21,41,71,180],[0,53,54,55,56,57,58,59,60,61,62]]
    data1=data1.set_axis(['Country','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False)
    data1.reset_index(drop=True, inplace=True)
    print(data1)
    data2=data1.set_index('Country').T
    print(data2)
    return data1, data2

import_data1,import_tdata1=Read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\fuel_import1.xlsx")
gdp_data2,gdp_tdata2=Read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\gdp.xlsx")

print("\n Statistics values of data: \n")
def Statistical_values(data_name):
    a=data_name.describe()
    return a

Statistical_values(import_tdata1)
Statistical_values(gdp_tdata2)

print("\n Imports and GDP of United Arab Emirates Correlation: \n")
print(import_tdata1['United Arab Emirates'].corr(gdp_tdata2['United Arab Emirates']))
print("\n Imports and GDP of Belgium Correlation: \n")
print(import_tdata1['Belgium'].corr(gdp_tdata2['Belgium']))
print("\n Imports and GDP of Switzerland Correlation: \n")
print(import_tdata1['Switzerland'].corr(gdp_tdata2['Switzerland']))
print("\n Imports and GDP of Egypt, Arab Rep. Correlation: \n")
print(import_tdata1['Egypt, Arab Rep.'].corr(gdp_tdata2['Egypt, Arab Rep.']))
print("\n Imports and GDP of Netherlands Correlation: \n")
print(import_tdata1['Netherlands'].corr(gdp_tdata2['Netherlands']))
print("\n Correlation of data between years: \n")


def plot_1(data_name,types):
    data_name.plot(kind=types)
          
plot_1(import_tdata1,"line")
plot_1(gdp_tdata2,"line")


plt.matshow(import_data1.corr())
plt.xticks(range(import_data1.select_dtypes(['number']).shape[1]), import_data1.select_dtypes(['number']).columns, fontsize=12, rotation=45)
plt.yticks(range(import_data1.select_dtypes(['number']).shape[1]), import_data1.select_dtypes(['number']).columns, fontsize=12)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=12)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

   
print("\n Correlation between various years of Fuel Import data: \n")
print(import_data1.corr())
print("\n Correlation between various years of GDP data: \n")
print(gdp_data2.corr())
