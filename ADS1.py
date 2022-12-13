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
export_data3,export_tdata3=Read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\fuel_export.xlsx")
gdp_data2,gdp_tdata2=Read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\gdp.xlsx")

def Line_plot(data_name,xlabel,ylabel,title):
    import_tdata1.plot(kind='line',label='Country Name')
    plt.xticks(rotation=45)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc='upper right')
    plt.show()

Line_plot(import_tdata1,'Year','Values','Fuel Import')
Line_plot(export_data3,'Year','Values','Fuel Eport')
Line_plot(gdp_tdata2,'Year','Values','GDP growth')
#defining a function for plotting various graphs.

def plot_1(data_name,types):
    data_name.plot(kind=types)
    
#plotting the Kernel density estimate function for the transposed datas.           
plot_1(import_tdata1,'kde') 
plot_1(export_tdata3,'kde')
plot_1(gdp_tdata2,'kde')


#printing the statistical properties of the data using Stastical_values function.
print("\n Statistics values of data: \n")

def Statistical_values(data_name):
    a=data_name.describe()
    return a

S1=Statistical_values(import_tdata1)
S2=Statistical_values(gdp_tdata2)
S3=Statistical_values(export_tdata3)
print(S1)
print(S2)
print(S3)

#printing the statistical properties of the data using Stastical_values function.
print("\n Correlation values of data: \n")

#defining a function for finding correlation between countries of given data.

def Correlation_years(data_name):
    b=data_name.corr()
    return b

#printing the values of correlation of transposed data.

C1=Correlation_years(import_tdata1)
C2=Correlation_years(gdp_tdata2)
C3=Correlation_years(export_tdata3)
print(C1)
print(C2)
print(C3)

print('\n Correlation between GDP and Fuel Import \n')
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
#printing the correlation between GDP and Fuel Export of various Countries.

print('\n Correlation between GDP and Fuel Export \n')
print("\n Exports and GDP of United Arab Emirates Correlation: \n")
print(export_tdata3['United Arab Emirates'].corr(gdp_tdata2['United Arab Emirates']))
print("\n Exports and GDP of Belgium Correlation: \n")
print(export_tdata3['Belgium'].corr(gdp_tdata2['Belgium']))
print("\n Exports and GDP of Switzerland Correlation: \n")
print(export_tdata3['Switzerland'].corr(gdp_tdata2['Switzerland']))
print("\n Exports and GDP of Egypt, Arab Rep. Correlation: \n")
print(export_tdata3['Egypt, Arab Rep.'].corr(gdp_tdata2['Egypt, Arab Rep.']))
print("\n Exports and GDP of Netherlands Correlation: \n")
print(export_tdata3['Netherlands'].corr(gdp_tdata2['Netherlands']))
