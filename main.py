import pandas as pd
import matplotlib.pyplot as plt

#Loading data
df = pd.read_excel("data/unclean_sales.xlsx")

def clean_data():
    df = pd.read_excel("data/unclean_sales.xlsx")
    # Handle missing values
    df['City'] = df['City'].fillna('Unknown')

    # Fix category typo
    df['Category'] = df['Category'].replace('Electroncs', 'Electronics')

    # Remove invalid rows
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert date
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])

    # Recalculate sales
    df['TotalSales'] = df['Quantity'] * df['UnitPrice']

    # Save cleaned data
    df.to_excel("data/cleaned_sales.xlsx", index=False)
    print("Cleaned data saved to cleaned_sales.xlsx")

    return df

#Sales by Category
def sales_by_category():
    data = df.groupby('Category')['TotalSales'].sum()
    plt.figure(figsize=(8,5))
    data.plot(kind='bar', color='steelblue')
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

#Sales by City
def sales_by_city():
    data = df.groupby('City')['TotalSales'].sum()
    plt.figure(figsize=(8,5))
    data.plot(kind='bar', color='darkorange')
    plt.title("Total Sales by City")
    plt.xlabel("City")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()


#Daily Sales Trend
def daily_sales_trend():
    data = df.groupby('OrderDate')['TotalSales'].sum()
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data.values, marker='o')
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#Monthly Sales Trend
def monthly_sales_trend():
    df['Month'] = df['OrderDate'].dt.to_period('M')
    data = df.groupby('Month')['TotalSales'].sum()
    plt.figure(figsize=(8,5))
    data.plot(kind='line', marker='o', color='green')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()


#Sales Distribution by Category
def category_sales_distribution():
    data = df.groupby('Category')['TotalSales'].sum()
    plt.figure(figsize=(6,6))
    data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title("Category-wise Sales Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

#Top 5 Products by Revenue
def top_products():
    data = df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(8,5))
    data.plot(kind='bar', color='purple')
    plt.title("Top 5 Products by Revenue")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

#distribution of order sales
def sales_histogram():
    plt.figure(figsize=(8,5))
    plt.hist(df['TotalSales'], bins=10, color='teal', edgecolor='black')
    plt.title("Distribution of Order Sales")
    plt.xlabel("Order Sales Amount")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

#category sales by city.
def stacked_category_city_sales():
    pivot_data = pd.pivot_table(
        df,
        values='TotalSales',
        index='City',
        columns='Category',
        aggfunc='sum'
    )

    pivot_data.plot(
        kind='bar',
        stacked=True,
        figsize=(9,6)
    )

    plt.title("Category-wise Sales by City")
    plt.xlabel("City")
    plt.ylabel("Total Sales")
    plt.legend(title="Category")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    clean_data()
    sales_by_category()
    sales_by_city()
    daily_sales_trend()
    monthly_sales_trend()
    category_sales_distribution()
    top_products()
    sales_histogram()
    stacked_category_city_sales()
