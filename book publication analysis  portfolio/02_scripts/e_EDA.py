#  the file a_library_imports.py  have all libraries importation and imported here  for avoiding repetitive imports.
from a_library_imports import *  

#the file b_data_loader have importation of of data set and creation of dataframe and imported here because dataframe will require for this file code and avoiding repeatative work
from b_data_loader import *

# importing the all parts from data cleaning for future analysis
from d_data_cleaning import *

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
