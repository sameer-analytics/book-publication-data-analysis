#  the file a_library_imports.py  have all libraries importation and imported here  for avoiding repetitive imports.
from a_library_imports import *  

df=pd.read_json("https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/books.json",lines=True) # converting the json data to data frame
print(df)