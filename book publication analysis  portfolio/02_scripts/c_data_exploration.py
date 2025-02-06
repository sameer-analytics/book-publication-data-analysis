
#  the file a_library_imports.py  have all libraries importation and imported here  for avoiding repetitive imports.
from a_library_imports import *  

#the file b_data_loader have importation of of data set and creation of dataframe and imported here because dataframe will require for this file code and avoiding repeatative work
from b_data_loader import *  

#data exploration>>>>>>>>>>>>>>
print(df.head(10))# for data pattern
print(df.tail(10))
print(df.columns)#columns name
print(len(df.columns))#total number of the column
#statistical information
print(df.describe())#pagecount column is numeric so it work on it only
#checking total no. of null values in df column wise and dtypes
print(df.isnull().sum())
print(df.info())