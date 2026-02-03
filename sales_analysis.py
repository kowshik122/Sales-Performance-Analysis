import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(
    r"C:\Users\user\OneDrive\Documents\sales_performance_analysis\dataset\Superstore.xlsx.xlsx"
)

print(df.head())
print(df.info())
print(df.describe())



df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)
plt.figure()
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("output/charts/monthly_sales.png")
plt.show()
category_profit = df.groupby('Category')['Profit'].sum()
print(category_profit)
plt.figure()
category_profit.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("output/charts/category_profit.png")
plt.show()
print("Highest Sales Month:", monthly_sales.idxmax())
print("Most Profitable Category:", category_profit.idxmax())
print("Least Profitable Category:", category_profit.idxmin())
category_profit = df.groupby('Category')['Profit'].sum()
print(category_profit)
print("Highest Sales Month:", monthly_sales.idxmax())
print("Most Profitable Category:", category_profit.idxmax())
print("Least Profitable Category:", category_profit.idxmin())
