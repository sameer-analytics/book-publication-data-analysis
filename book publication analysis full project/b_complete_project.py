#importing required  libraries and module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
#steps 
#converting the json data into a df
#explore the data
#clean and manipulate the data
#analysis of data EDA
#insights
#conclusion
df=pd.read_json("https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/books.json",lines=True)
print(df)

#data exploration>>>>>>>>>>>>>>
print(df.head(10))
print(df.tail(10))
print(df.columns)#columns name
print(len(df.columns))#total number of the column
#statistical information
print(df.describe())#pagecount column is numeric so it work on it only
#checking total no. of null values in df column wise and dtypes
print(df.isnull().sum())
print(df.info())

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

#EXPLORATORY DATA ANALYSIS:-
#Exploring the distribution of page count using histogram
plt.hist(df["pageCount"], bins=20, edgecolor="k")
plt.title("Distribution ofpage count")
plt.xlabel("page Count")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#Exploring the publication of books per year
book_per_year=df.groupby("publishedYear").agg({"book title":"count"}).reset_index()
book_per_year.rename(columns={"book title":"number of books"},inplace=True)


plt.bar(book_per_year["publishedYear"], book_per_year["number of books"], color="b", edgecolor="k", hatch="//")
plt.xlabel("publishedYear", color="b", size=15)  # Label for the x-axis
plt.ylabel("number of books", color="b", size=15)  # Label for the y-axis
plt.title("Number of Book Published Per Year", color="m", size=15)  # Title for the chart
plt.grid()  # Displaying grid lines
plt.show()  # Display the plot

#Exploring the most 10  author by book publication
athr=df.groupby("authors").agg({"book title":"count"}).reset_index()
athr.rename(columns={"book title":"number of books"},inplace=True)
book_by_author=athr.sort_values(by="number of books",ascending=False).head(10) 

plt.bar(book_by_author["authors"], book_by_author["number of books"], color="b", edgecolor="k", hatch="//")
plt.xlabel("author", color="b", size=15)  # Label for the x-axis
plt.ylabel("number of books", color="b", size=15)  # Label for the y-axis
plt.title("Number of Book Published by author", color="m", size=15)  # Title for the chart
plt.grid()  # Displaying grid lines
plt.show()  # Display the plot

#exploring the co-realation between published year vs page count
plt.scatter(df["publishedYear"], df["pageCount"], color="darkgreen", s=20)
plt.xlabel("published year",color="b", size=15)  # Label for the x-axis
plt.ylabel("page count",color="b", size=15)  # Label for the y-axis
plt.title("published year vs page count", color="m", size=15)  # Title for the chart
plt.show()  # Display the plot


#Data Visualization and insights(combo)

# 1. Books Published Per Year (Bar Chart)
plt.figure(figsize=(12, 6))
df['publishedYear'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.xlabel("Publication Year")
plt.ylabel("Number of Books")
plt.title("Books Published Per Year")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Insight 1: The number of books published fluctuates over the years. This can indicate trends such as industry growth, technological advancements, or economic factors affecting publishing rates.

# 2. Distribution of Book Lengths (Histogram)
plt.figure(figsize=(10, 5))
df['pageCount'].hist(bins=30, color='green', edgecolor='black')
plt.xlabel("Page Count")
plt.ylabel("Frequency")
plt.title("Distribution of Book Lengths")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Insight 2: Most books fall within a certain page range, suggesting a preferred book length by publishers and readers. Outliers with very high or low page counts might indicate niche genres or special editions.

# 3. Top 10 Authors with Most Books (Bar Chart)
df['authors'] = df['authors'].str.replace("'", "")  # Clean author names
author_counts = df['authors'].value_counts().nlargest(10)
plt.figure(figsize=(12, 6))
author_counts.plot(kind='barh', color='purple')
plt.xlabel("Number of Books Published")
plt.ylabel("Authors")
plt.title("Top 10 Authors with Most Books")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Insight 3: A few authors dominate the publishing industry by producing a significantly higher number of books. This might indicate high demand for their work or prolific writing habits.

# 4. Publication Status Distribution (Pie Chart)
plt.figure(figsize=(8, 5))
df['status'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'orange', 'lightgreen'], startangle=140)
plt.title("Publication Status Distribution")
plt.ylabel("")
plt.show()

# Insight 4: The majority of books fall under a particular publication status (e.g., published, unpublished, or pending). This can reflect market demand and the efficiency of the publishing process.

# 5. Average Page Count Per Year (Line Chart)
avg_page_count = df.groupby('publishedYear')['pageCount'].mean()
plt.figure(figsize=(12, 6))
plt.plot(avg_page_count.index, avg_page_count.values, marker='o', linestyle='-', color='red')
plt.xlabel("Publication Year")
plt.ylabel("Average Page Count")
plt.title("Average Page Count Per Year")
plt.grid()
plt.show()

# Insight 5: The average length of books changes over time, possibly due to shifts in reader preferences, industry standards, or trends in storytelling formats.

# 6. Books Published by Year & Status (Stacked Bar Chart)
status_counts = df.groupby(['publishedYear', 'status']).size().unstack()
status_counts.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))
plt.xlabel("Publication Year")
plt.ylabel("Number of Books")
plt.title("Books Published by Year and Status")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title="Status")
plt.show()

# Insight 6: The distribution of book publication statuses varies over time. A rise or decline in specific statuses can indicate shifts in publishing strategies, market conditions, or regulatory changes.



