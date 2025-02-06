#  the file a_library_imports.py  have all libraries importation and imported here  for avoiding repetitive imports.
from a_library_imports import *  

#the file b_data_loader have importation of of data set and creation of dataframe and imported here because dataframe will require for this file code and avoiding repeatative work
from b_data_loader import * 

#data cleaning>>>>>
#1)cleaning the isbn column
#listing the rows which have nan in df accoding to isbn column
d=df[df["isbn"].isna()]
print(d)
def clean(ext):
    x=re.sub("[A-Z]|[a-z]|-","",str(ext))
    return(x)
df["isbn"]=df["isbn"].apply(clean)#it clean the the column 
#we dont required the isbn number so it better to delete the column
lc=df[df["isbn"].isna()]
print(lc)
df.drop("isbn",axis=1,inplace=True)#it will drop isbn column

#2)checking is there any clean need in tittle column
print(df.title.unique())
d=df[df.duplicated(subset="title")]
print(d)
#check the row vlaues of repeated values in tittle column have same data in other columns or not 
ls=["Jaguar Development with PowerBuilder 7","SQL Server MVP Deep Dives","Android in Practice"]
r=df[df["title"].isin(ls)]
print(r)
#droping all duplicates row according to tittle column
df.drop_duplicates(subset="title",inplace=True)
df["title"]=df["title"].astype("string")

#3)handling the id column
df["_id"]=range(1,len(df["_id"])+1)#changing id from 1 to end
print(df._id)
df.reset_index(drop=True,inplace=True)#reset the index due to drop of duplicate rows

#4)handling the page count column >>replacing the the 0 places of pageCount with the mean of the pagecount column
df["pageCount"]=df["pageCount"].replace({0:int(df.pageCount.mean())})#replacing the the 0 places of pageCount with the mean of the pagecount column

#5)cleaning the publish date column
print(df["publishedDate"].isna().sum())#checking the nan values
df["publishedDate"]=df["publishedDate"].fillna(0)#replacing nan with 0
y=df["publishedDate"].iloc[0]
cd=re.sub("^{.*: '|-.*}","",str(y))#testing to clean a single value of the column
print(cd)
#cleanig the column publishdate using function and re
def cln(dt):
    i=int(re.sub("^{.*: '|-.*}","",str(dt)))
    return i
df["publishedDate"]=df["publishedDate"].apply(cln)
df["publishedDate"]=df["publishedDate"].replace(0,round(df["publishedDate"].mean()))#replacing the 0 with mean of the column publishdate
print(df["publishedDate"])
df.rename(columns={"publishedDate":"publishedYear"},inplace=True)#rename the column because we clean the column and got only year so we need to rename
print(df["publishedYear"])

#6)removing the unwanted columns(thumbnailUrl,shortDescription,longDescription)
df.drop(["thumbnailUrl","shortDescription","longDescription"],axis=1,inplace=True)
print(df)

#7)handling the status column
print(df["status"].unique())#checking the unique and got PUBLISH and MEAP
print(df["status"].isna().sum())#checking is there any nan value in status column
print(df.status.value_counts())#calculating the number of publish and meap present in the column
df["status"]=df["status"].replace("MEAP","UNPUBLISH")#replacing MEAP with UNPUBLISH
df["status"]=df["status"].astype("string")#typecasting the status

#8)cleaning the authors column
x=df.authors.apply(lambda y:y==[]).sum()#calculating the empty list present in the column authors
print(x)
df["authors"] = df["authors"].apply(lambda x: "unknown" if len(x) == 0 else x)
#cleaning the column using regex
def cn(d):
    t=re.sub(r"\[|\]","",str(d))
    return t
df["authors"]=df["authors"].apply(cn)
df["authors"]=df["authors"].astype("string")#typecasting the autor column to string

#9)conclude that the categories column is not required for analysis so we need to drop it as well
df.drop(["categories"],axis=1,inplace=True)
print(df.info())

#renaming the title column to book title for future analysis
df.rename({"title":"book title"},axis=1,inplace=True)
print(df)
# df.to_csv(r"C:\Users\HP\Desktop\book publication analysis.csv",index=False)