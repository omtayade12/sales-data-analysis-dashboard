import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert date column
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

# Print summary
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nMonthly Sales:")
print(df.groupby("Month")["Sales"].sum())

# Create charts
df.groupby("Category")["Sales"].sum().plot(kind="bar", title="Sales by Category")
plt.savefig("sales_by_category.png")
plt.close()

df.groupby("Region")["Sales"].sum().plot(kind="bar", title="Sales by Region")
plt.savefig("sales_by_region.png")
plt.close()

df.groupby("Month")["Sales"].sum().plot(marker="o", title="Monthly Sales Trend")
plt.savefig("monthly_sales.png")
plt.close()

print("\nCharts saved successfully")
