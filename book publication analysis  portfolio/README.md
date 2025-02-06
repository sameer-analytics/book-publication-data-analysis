# Book Publication Analysis

## Project Overview
This project focuses on analyzing book publication data to uncover insights about publishing trends, author contributions, and book characteristics. The dataset used for this analysis is sourced from a JSON file containing information about various books.

## Dataset
The dataset includes details about books such as titles, authors, publication dates, page counts, categories, and publication statuses.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Regular Expressions (re)

## Folder Structure
Book_Publication_Analysis/ (Main project folder containing all files and scripts)  
- data/ (Folder for storing dataset files)  
  - a_dat_souce.txt(contais the json data link) 
  - b_book_publication_cleaned_dataset.csv(this contain the cleaned dataset)
- script/ (Folder containing Python scripts for different stages of analysis) 
  - a_library_imports.py(conatins all the imported libraries) 
  - b_data_loader.py(contains dataframe)
  - c_data_exploration(contsins exploration part)
  - d_data_cleaning.py (Script for cleaning and preprocessing the dataset)  
  - e_eda.py (Script for performing exploratory data analysis)  
  - f_visualization.py (Script for generating visualizations)  
- output/
  - (contains 01_visualizations(images)/ which have the png files of the visualizations)
  - 02_reports(contains the insights.md which describes the insights of the project )
- README.md (Project documentation file)  
- requirements.txt (File listing required libraries)  

## Steps Involved

### Data Loading
- Convert the JSON data into a DataFrame.

### Data Exploration
- Display dataset structure and statistical summaries.
- Identify missing values and data types.

### Data Cleaning & Manipulation
- Handle missing values.
- Clean the isbn, title, id, pageCount, publishedDate, status, and authors columns.
- Remove unnecessary columns (thumbnailUrl, shortDescription, longDescription, categories).

### Exploratory Data Analysis (EDA)
- Understand book distribution by page count, publication year, and author contributions.

### Insights & Visualizations
- Identify key trends in book publications.
- Visualize relationships between different variables.

## Conclusion
Summarize key findings and potential implications.

### Data Exploration
- Display first and last 10 rows of the dataset.
- Identify column names and count.
- Compute statistical summary for numerical columns.
- Check for missing values and data types.

### Data Cleaning
- Remove unwanted characters from isbn and drop the column.
- Remove duplicate book titles while ensuring data consistency.
- Normalize the id column to maintain a sequential range.
- Replace zero page counts with the mean page count.
- Extract and clean publishedYear from publishedDate.
- Standardize the status column (e.g., replace MEAP with UNPUBLISH).
- Ensure authors column has valid values and clean formatting.

### Exploratory Data Analysis (EDA)
1. Distribution of Page Counts  
   - Histogram visualization to analyze book length distribution.  

2. Books Published Per Year  
   - Bar chart showing the number of books published annually.  

3. Top 10 Authors by Number of Books  
   - Identify the most prolific authors through a bar chart.  

4. Publication Status Distribution  
   - Pie chart displaying the proportion of published vs. unpublished books.  

5. Average Page Count Over Time  
   - Line chart showing how book lengths have evolved over the years.  

6. Books Published by Year & Status  
   - Stacked bar chart analyzing publication trends over time.  

## Insights
- The publishing industry exhibits fluctuating trends in book releases.
- Most books fall within a certain page count range, reflecting common publishing standards.
- A few authors dominate book publishing with significantly higher contributions.
- Publication status trends indicate variations in publishing strategies.
- Changes in average book length might reflect evolving reader preferences and industry trends.

## Conclusion
This analysis provides valuable insights into book publication trends, helping publishers, authors, and researchers understand industry patterns. Further analysis can explore genre-specific trends or deeper author contributions.


