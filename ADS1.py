import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#function for reading the data from 2009 to 2018 for 5 countries.
def Read_data1(file_name1):
    data1=pd.read_excel(file_name1)
    data1=data1.iloc[[12,21,41,71,180],[0,53,54,55,56,57,58,59,60,61,62]]
    data1=data1.set_axis(['Country','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False)
    data1.reset_index(drop=True, inplace=True)
    print(data1)
    data2=data1.set_index('Country').T
    print(data2)
    return data1, data2
#read the data using function.
import_data1,import_tdata1=Read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\fuel_import1.xlsx")
gdp_data2,gdp_tdata2=Read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\gdp.xlsx")
#printing the statistical properties of the data using Stastical_values function.
print("\n Statistics values of data: \n")

def Statistical_values(data_name):
    a=data_name.describe()
    return a

Statistical_values(import_tdata1)
Statistical_values(gdp_tdata2)
#printing the correlation between GDP and Fuel Import of various Countries.
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

#defining a function for plotting various graphs.

def plot_1(data_name,types):
    data_name.plot(kind=types)
    
#plotting the Line graphs and Kernel density estimate function for the transposed datas.
           
plot_1(import_tdata1,"line")
plot_1(gdp_tdata2,"line")
plot_1(import_tdata1,'kde')
plot_1(gdp_tdata2,'kde')

#plotting Correlation matrix between the years of fuel import data.
plt.matshow(import_data1.corr())
plt.xticks(range(import_data1.select_dtypes(['number']).shape[1]), import_data1.select_dtypes(['number']).columns, fontsize=12, rotation=45)
plt.yticks(range(import_data1.select_dtypes(['number']).shape[1]), import_data1.select_dtypes(['number']).columns, fontsize=12)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=12)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

 #printing the correlation between various years of the above data.  
print("\n Correlation between various years of Fuel Import data: \n")
print(import_data1.corr())
print("\n Correlation between various years of GDP data: \n")
print(gdp_data2.corr())
print("\n Correlation of data between Countries: \n")

#defining a function for finding correlation between countries of given data.

def Correlation_years(data_name):
    b=data_name.corr()
    return b

#printing the values of correlation of transposed data.

Correlation_years(import_tdata1)
Correlation_years(gdp_tdata2)

