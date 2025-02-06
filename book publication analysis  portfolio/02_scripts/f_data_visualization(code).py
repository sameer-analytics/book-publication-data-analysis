
#  the file a_library_imports.py  have all libraries importation and imported here  for avoiding repetitive imports.
from a_library_imports import *  

df=pd.read_json("https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/books.json",lines=True) # converting the json data to data frame
print(df)

# importing the all parts from data cleaning for future analysis
from d_data_cleaning import *

#Data Visualization 
# 1. Books Published Per Year (Bar Chart)
plt.figure(figsize=(12, 6))
df['publishedYear'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.xlabel("Publication Year")
plt.ylabel("Number of Books")
plt.title("Books Published Per Year")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Distribution of Book Lengths (Histogram)
plt.figure(figsize=(10, 5))
df['pageCount'].hist(bins=30, color='green', edgecolor='black')
plt.xlabel("Page Count")
plt.ylabel("Frequency")
plt.title("Distribution of Book Lengths")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

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

# 4. Publication Status Distribution (Pie Chart)
plt.figure(figsize=(8, 5))
df['status'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'orange', 'lightgreen'], startangle=140)
plt.title("Publication Status Distribution")
plt.ylabel("")
plt.show()

# 5. Average Page Count Per Year (Line Chart)
avg_page_count = df.groupby('publishedYear')['pageCount'].mean()
plt.figure(figsize=(12, 6))
plt.plot(avg_page_count.index, avg_page_count.values, marker='o', linestyle='-', color='red')
plt.xlabel("Publication Year")
plt.ylabel("Average Page Count")
plt.title("Average Page Count Per Year")
plt.grid()
plt.show()

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