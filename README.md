E-Commerce Sales Analysis Project Report

1. Project Overview
Project Title: E-Commerce Sales Analysis
Objective:
The goal of this project is to analyse e-commerce sales data, clean noisy datasets, calculate key metrics, and visualize insights for better business decision-making.
Dataset Description:
•	The dataset contains 100 records of e-commerce transactions.
•	Columns included:
o	OrderID – Unique identifier for each order
o	Product – Name of the product sold
o	Category – Product category (Electronics, Clothing, etc.)
o	Quantity – Number of units sold
o	UnitPrice – Price per unit
o	City – City where order was placed
o	OrderDate – Date of the order
o	TotalSales – Calculated as Quantity × UnitPrice
Tools Used:
•	Python 3.14
•	Pandas (for data manipulation)
•	Matplotlib (for data visualization)
•	Microsoft Excel (for dataset and cleaned output)


2. Project Workflow
The project was executed in 7 steps, following a structured approach:

Day	Activity
1-2	Project Setup: Topic selection, data collection, folder structure creation
3	Data Exploration: Load data, handle missing values, clean noisy data
4	Basic Analysis: Calculate metrics, summarize key insights
5	Data Visualization: Create charts and graphs using Matplotlib
6	Report Creation: Combine analysis and visuals into a document
7	Finalization: Test code, fix errors, and prepare final submission

3. Data Cleaning Process
The dataset contained some inconsistencies and errors, which were handled as follows:
1.	Handling Missing Values:
o	Missing city names were replaced with "Unknown".
2.	Correcting Typographical Errors:
o	Typo in the Category column: "Electroncs" → "Electronics".
3.	Removing Invalid Entries:
o	Rows with Quantity <= 0 or UnitPrice <= 0 were removed.
4.	Removing Duplicates:
o	Duplicate orders were dropped.
5.	Converting Date Column:
o	OrderDate column converted to datetime format.
6.	Calculating Total Sales:
o	Added a new column: TotalSales = Quantity × UnitPrice.
7.	Saving Cleaned Dataset:
o	Cleaned data was saved as cleaned_sales.xlsx in the data folder.
4. Basic Analysis
After cleaning, basic metrics were calculated:
•	Total Revenue: Sum of all orders (TotalSales)
•	Average Order Value: Mean of all TotalSales
•	Sales by Category: Total sales aggregated per category
•	Sales by City: Total sales aggregated per city
•	Daily Sales Trend: Total sales per day
These metrics helped to identify high-performing categories, cities, and order patterns.


5 Technical Details
5.1 Architecture Overview
The project follows a modular data analysis pipeline:
Raw Data (unclean_sales.xlsx)
           │
          ▼
   Data Cleaning & Preprocessing
           │
          ▼
   Cleaned Dataset (cleaned_sales.xlsx)
           │
          ▼
   Data Analysis & Metrics
           │
          ▼
   Visualizations (Charts & Graphs)
           │
          ▼
   Insights & Report
Components:
1.	Data Layer:
o	Input: unclean_sales.xlsx
o	Output: cleaned_sales.xlsx
2.	Processing Layer:
o	Cleaning functions (clean_data)
o	Aggregation and calculation of metrics (TotalSales, groupings by category/city/month)
3.	Visualization Layer:
o	Individual chart functions for modular plotting
o	Each function reads cleaned data to ensure consistency
4.	Output Layer:
o	Charts displayed via Matplotlib
o	Report written manually in Word (with placeholders for images)

5.2 Data Structures Used
1.	Pandas DataFrame
o	Core data structure for tabular data
o	Provides built-in support for filtering, grouping, aggregation, and date manipulation
o	Example: df.groupby('Category')['TotalSales'].sum()
2.	Pivot Table (for stacked bar chart)
o	Converts long-form data into a matrix of cities vs categories
o	Used for generating stacked visualizations
3.	Lists/Arrays (within Matplotlib)
o	Used internally for plotting (plt.plot(x, y))
4.	Dictionary-like Structures
o	Pandas grouping results behave like dictionaries for quick mapping from keys (e.g., category) to aggregated values

5.3 Algorithms / Computation
Data Cleaning Algorithm
1.	Load raw Excel file into a Pandas DataFrame
2.	Replace missing City values with "Unknown"
3.	Correct typos in Category
4.	Remove invalid rows (negative or zero Quantity or UnitPrice)
5.	Remove duplicate rows
6.	Convert OrderDate column to datetime format
7.	Compute TotalSales = Quantity × UnitPrice
8.	Save cleaned data to Excel
Pseudocode:
load df from Excel
df['City'].fillna('Unknown')
df['Category'].replace('Electroncs', 'Electronics')
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df.drop_duplicates()
df['OrderDate'] = to_datetime(df['OrderDate'])
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
save df to cleaned_sales.xlsx

Aggregation Algorithm
•	Group by Column(s) using Pandas groupby
•	Compute sum, mean, or count for analysis
•	Example:
# Total sales per category
category_sales = df.groupby('Category')['TotalSales'].sum()
•	Complexity:
o	O(n) for a dataset of n rows

Visualization Logic
•	Each chart function is modular:
o	Input: cleaned DataFrame
o	Process: aggregate or pivot data as needed
o	Output: chart displayed with Matplotlib
•	Chart Types & Techniques:
o	Bar chart → df.groupby().sum().plot(kind='bar')
o	Line chart → df.groupby().sum().plot(kind='line')
o	Pie chart → df.groupby().sum().plot(kind='pie')
o	Histogram → plt.hist(df['TotalSales'])
o	Stacked Bar → pd.pivot_table(df, index='City', columns='Category').plot(stacked=True)

5.4 Software & Libraries Architecture
Layer	Library / Tool	Role
Data Processing	Pandas	Load, clean, filter, aggregate, pivot
Visualization	Matplotlib	Bar, line, pie, histogram, stacked charts
File Handling	Python os, Excel I/O	Read/write Excel files
Reporting	Word (manual)	Documenting results

5.5 Key Advantages of This Architecture
•	Modular: Each function (cleaning, visualization) works independently
•	Reproducible: Cleaned dataset is saved and reused for all charts
•	Scalable: Can handle larger datasets with minimal changes
•	Easy to Explain: Each layer corresponds to a logical step in real-world data analytics pipeline

6. Visualizations
The following visualizations were created to provide insights into sales patterns. (Images to be inserted later)
6.1 Sales by Category (Bar Chart)
Purpose: Compare total sales across different product categories.
Observation: Electronics and Clothing are the highest-selling categories.

6.2 Sales by City (Bar Chart)
Purpose: Compare total sales across different cities.
Observation: Some cities generate significantly higher revenue than others.

6.3 Daily Sales Trend (Line Chart)
Purpose: Observe sales trends on a day-to-day basis.
Observation: Peaks in sales may indicate promotions or bulk orders.

6.4 Monthly Sales Trend (Line Chart)
Purpose: Identify monthly seasonality in sales.
Observation: Some months show higher total revenue due to special events or sales campaigns.
 
6.5 Category-wise Sales Distribution (Pie Chart)
Purpose: Understand each category’s contribution to overall sales.
Observation: Electronics dominates the total revenue share.

6.6 Top 5 Products by Revenue (Bar Chart)
Purpose: Identify the best-selling products by total revenue.
Observation: Top 5 products account for a major portion of total sales.
 
6.7 Distribution of Order Sales (Histogram)
Purpose: Understand the distribution of sales per order.
Observation: Most orders are of lower value, with a few high-value orders

6.8 Category Sales by City (Stacked Bar Chart)
Purpose: Compare contribution of each category to total sales per city.
Observation: Some categories perform better in specific cities.

7. Conclusion & Insights
•	Highest Performing Category: Electronics consistently contributed the highest revenue.
•	High Revenue Cities: Certain cities generated significantly higher sales; targeted marketing can further enhance revenue.
•	Sales Patterns: Daily and monthly trends highlight peaks and low periods for inventory planning.
•	Product Focus: Top 5 products generate a large portion of revenue; stock and promotions should prioritize these.
Next Steps / Recommendations:
1.	Conduct deeper analysis on customer purchase patterns.
2.	Introduce targeted promotions based on high-performing cities.
3.	Forecast future sales using historical trends.
4.	Use heatmaps or advanced dashboards for real-time monitoring.

8. Project Structure
•	Cleaned Dataset: cleaned_sales.xlsx
•	Uncleaned Dataset: unclean_datset/xlsx
•	Python Code: main.py All cleaning and visualization scripts.
•	Report. Report.docx
•	Folder Structure:
ecommerce_sales_analysis/
├── data/
   ├── unclean_sales.xlsx
     └── cleaned_sales.xlsx
├── visuals/
├── main.py
 └── report.docx


