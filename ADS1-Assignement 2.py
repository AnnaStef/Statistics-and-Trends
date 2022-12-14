import pandas as pd # Importing the pandas library as pd
import matplotlib.pyplot as plt # Importing the matplot.pyplot library as plt
import numpy as np # Importing the numpy library as np

#function for reading the data from 2009 to 2018 for 5 countries.
def read_data1(file_name1): # Definig a function to read the file
    data1=pd.read_excel(file_name1) # To read the file
    data1=data1.iloc[[12,21,41,71,180],[0,53,54,55,56,57,58,59,60,61,62]] # To select desired rows and columns using iloc function
    data1=data1.set_axis(['Country','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False) # To assign desired index to given axis
    data1.reset_index(drop=True, inplace=True) # Resetting the index values
    print(data1) # Printing the data
    data2=data1.set_index('Country').T # Transposing the data
    print(data2) # printing the transposed data
    return data1, data2 # returning the data

#reading the data using function.
import_data1,import_tdata1=read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\fuel_import1.xlsx")
export_data3,export_tdata3=read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\fuel_export.xlsx")
gdp_data2,gdp_tdata2=read_data1("C:\\Users\\shobi\\ADS Asgnmt\\Anna\\gdp.xlsx")

def line_plot(data_name,xlabel,ylabel,title): # Defining a function for line plot
    import_tdata1.plot(kind='line',label='Country Name') # Importing the dataframe
    plt.xticks(rotation=45) # Setting the angle of axis names
    plt.xlabel(xlabel) # TO Label the X-Axis
    plt.ylabel(ylabel) # To Label the Y-Axis
    plt.title(title) # To give the title for the graph
    plt.legend(loc='upper right') # To determine the index
    plt.show() # To Show the graph

# To plot the graphs by using defination
line_plot(import_tdata1,'Year','Values','Fuel Import')
line_plot(export_data3,'Year','Values','Fuel Eport')
line_plot(gdp_tdata2,'Year','Values','GDP growth')

# Creating a defination for density plot
def plot_1(data_name,types):
    data_name.plot(kind=types)
    
#plotting the Kernel density estimate function for the transposed datas using plot_1 function.           
plot_1(import_tdata1,'kde') # Plotting kde graph by importing required data
plot_1(export_tdata3,'kde') # Plotting kde graph by importing required data
plot_1(gdp_tdata2,'kde') # Plotting kde graph by importing required data

#defining and printing the statistical properties of the data using stastical_values function.
print("\n Statistics values of data: \n")

# Creating a defination fuction for finding the statistical values
def statistical_values(data_name):
    a=data_name.describe()
    return a

s1=statistical_values(import_tdata1) # Calling the Statistical defination function using desired dataset
s2=statistical_values(gdp_tdata2) # Calling the Statistical defination function using desired dataset
s3=statistical_values(export_tdata3) # Calling the Statistical defination function using desired dataset
print(s1) # Printing the statistical values of s1 
print(s2) # printing the statistical values of s2
print(s3) # printing the statistical values of s2

print("\n Correlation values of data: \n")

#defining a function for finding correlation between countries of given data and printing it.
def correlation_years(data_name):
    b=data_name.corr()
    return b

c1=correlation_years(import_tdata1) # Calling the correlation defination function using desired dataset
c2=correlation_years(gdp_tdata2) # Calling the correlation defination function using desired dataset
c3=correlation_years(export_tdata3) # Calling the correlation defination function using desired dataset
print(c1) # Printing the correlation values of c1
print(c2) # Printing the correlation values of c2
print(c3) # Printing the correlation values of c3

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