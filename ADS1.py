# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:41:00 2022

@author: shobi
"""

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

print(import_data1)
print(import_tdata1)
print(gdp_data2)
print(gdp_tdata2)
print(import_data1.describe())
print(gdp_data2.describe())


def plot_1(name,types):
    name.plot(kind=types)
          
plot_1(import_tdata1,"line")
plot_1(gdp_tdata2,"line")
