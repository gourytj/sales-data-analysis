# ==========================================
# 1. IMPORT LIBRARIES
# ==========================================
import pandas as pd

# ==========================================
# 2. LOAD DATASET
# ==========================================
data = pd.read_csv("sales_data project.csv")

# Check columns
print(data.columns)

# Check data information
print(data.info())

# Check duplicate rows
print("Duplicate rows:", data.duplicated().sum())

# Calculate sales
data["Sales"] = data["Qty"] * data["Price"]


# ==========================================
# 3. DATA CALCULATIONS
# ==========================================

#  Calculate Total Sales
total_sales = data["Sales"].sum()

print("Total Sales:", total_sales)

# Calculate Total Cost
data["Total_Cost"] = data["Qty"] * data["Cost"]

total_cost = data["Total_Cost"].sum()

print("Total Cost:", total_cost)

# Calculate Profit
data["Profit"] = data["Sales"] - data["Total_Cost"]

total_profit = data["Profit"].sum()

print("Total Profit:", total_profit)

#Calculate Total Quantity
total_quantity = data["Qty"].sum()

print("Total Quantity:", total_quantity)

# Calculate Total Orders
total_orders = len(data)

print("Total Orders:", total_orders)

# ==========================================
# 4. SALES AND PROFIT ANALYSIS
# ==========================================

# Sales by Location
sales_by_location = data.groupby("Location")["Sales"].sum()

print("\nSales by Location:")
print(sales_by_location)

#location with the highest sales
highest_sales_location = sales_by_location.idxmax()
highest_sales_value = sales_by_location.max()

print("\nHighest Sales Location:", highest_sales_location)
print("Highest Sales Value:", highest_sales_value)

#Sales by Product
sales_by_product = data.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(sales_by_product)

#product with the highest sales
highest_sales_product = sales_by_product.idxmax()
highest_product_sales = sales_by_product.max()

print("\nHighest Sales Product:", highest_sales_product)
print("Highest Product Sales:", highest_product_sales)

#Profit by Location
profit_by_location = data.groupby("Location")["Profit"].sum()

print("\nProfit by Location:")
print(profit_by_location)

#location with the highest profit
highest_profit_location = profit_by_location.idxmax()
highest_profit_value = profit_by_location.max()

print("\nHighest Profit Location:", highest_profit_location)
print("Highest Profit Value:", highest_profit_value)

#Profit by Product
profit_by_product = data.groupby("Product")["Profit"].sum()

print("\nProfit by Product:")
print(profit_by_product)

#product with the highest profit
highest_profit_product = profit_by_product.idxmax()
highest_product_profit = profit_by_product.max()

print("\nHighest Profit Product:", highest_profit_product)
print("Highest Product Profit:", highest_product_profit)

#product with the lowest profit
lowest_profit_product = profit_by_product.idxmin()
lowest_profit = profit_by_product.min()

print("Lowest Profit Product:", lowest_profit_product)
print("Lowest Product Profit:", lowest_profit)

# Sales by Product
highest_sales_product = sales_by_product.idxmax()
highest_sales = sales_by_product.max()

lowest_sales_product = sales_by_product.idxmin()
lowest_sales = sales_by_product.min()

print("Highest Sales Product:", highest_sales_product)
print("Highest Product Sales:", highest_sales)

print("Lowest Sales Product:", lowest_sales_product)
print("Lowest Product Sales:", lowest_sales)

# Converting Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

#Sales by Year
sales_by_year = data.groupby(data["Date"].dt.year)["Sales"].sum()

print("Sales by Year:")
print(sales_by_year)

#year with the highest sales
highest_sales_year = sales_by_year.idxmax()
highest_year_sales = sales_by_year.max()

print("Highest Sales Year:", highest_sales_year)
print("Highest Year Sales:", highest_year_sales)

#Sales by Month
sales_by_month = data.groupby(data["Date"].dt.month)["Sales"].sum()

print("Sales by Month:")
print(sales_by_month)

#month with the highest sales
highest_sales_month = sales_by_month.idxmax()
highest_month_sales = sales_by_month.max()

print("Highest Sales Month:", highest_sales_month)
print("Highest Month Sales:", highest_month_sales)

#Sales by Location
print("Sales by Location:")
print(sales_by_location)

#location with the lowest sales
lowest_sales_location = sales_by_location.idxmin()
lowest_location_sales = sales_by_location.min()

print("Lowest Sales Location:", lowest_sales_location)
print("Lowest Location Sales:", lowest_location_sales)

#Profit by Location
print("Profit by Location:")
print(profit_by_location)

#location with the lowest profit
lowest_profit_location = profit_by_location.idxmin()
lowest_location_profit = profit_by_location.min()

print("Lowest Profit Location:", lowest_profit_location)
print("Lowest Location Profit:", lowest_location_profit)

#Quantity sold by Product
qty_by_product = data.groupby("Product")["Qty"].sum()

print("Quantity by Product:")
print(qty_by_product)

#product with the highest quantity sold
highest_qty_product = qty_by_product.idxmax()
highest_qty = qty_by_product.max()

print("Highest Quantity Product:", highest_qty_product)
print("Highest Quantity Sold:", highest_qty)

#product with the lowest quantity sold
lowest_qty_product = qty_by_product.idxmin()
lowest_qty = qty_by_product.min()

print("Lowest Quantity Product:", lowest_qty_product)
print("Lowest Quantity Sold:", lowest_qty)

#average sales per order
average_sales_per_order = data["Sales"].mean()

print("Average Sales per Order:", average_sales_per_order)

#average profit per order
average_profit_per_order = data["Profit"].mean()

print("Average Profit per Order:", average_profit_per_order)


# ==========================================
# 5. PROFIT MARGIN ANALYSIS
# ==========================================

profit_margin = (data["Profit"].sum() / data["Sales"].sum()) * 100

print("Profit Margin:", profit_margin, "%")

# profit margin by location
profit_margin_by_location = (
    data.groupby("Location")["Profit"].sum()
    / data.groupby("Location")["Sales"].sum()
) * 100

print("Profit Margin by Location:")
print(profit_margin_by_location)

#location with highest profit margin
highest_margin_location = profit_margin_by_location.idxmax()
highest_margin = profit_margin_by_location.max()

print("Highest Profit Margin Location:", highest_margin_location)
print("Highest Profit Margin:", highest_margin, "%")

#location with lowest profit margin
lowest_margin_location = profit_margin_by_location.idxmin()
lowest_margin = profit_margin_by_location.min()

print("Lowest Profit Margin Location:", lowest_margin_location)
print("Lowest Profit Margin:", lowest_margin, "%")

# profit margin by product
profit_margin_by_product = (
    data.groupby("Product")["Profit"].sum()
    / data.groupby("Product")["Sales"].sum()
) * 100

print("Profit Margin by Product:")
print(profit_margin_by_product)

#product with highest profit margin
highest_margin_product = profit_margin_by_product.idxmax()
highest_product_margin = profit_margin_by_product.max()

print("Highest Profit Margin Product:", highest_margin_product)
print("Highest Product Profit Margin:", highest_product_margin, "%")

# product with lowest profit margin
lowest_margin_product = profit_margin_by_product.idxmin()
lowest_product_margin = profit_margin_by_product.min()

print("Lowest Profit Margin Product:", lowest_margin_product)
print("Lowest Product Profit Margin:", lowest_product_margin, "%")


# ==========================================
# 6. DATA VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt

# Sales by Location chart
sales_by_location.plot(kind="bar")

plt.title("Sales by Location")
plt.xlabel("Location")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by Product chart
sales_by_product.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Sales Trend
sales_by_month.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(sales_by_month.index)
plt.tight_layout()
plt.show()

# Profit by Product chart
profit_by_product.plot(kind="bar")

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit by Location chart
profit_by_location.plot(kind="bar")

plt.title("Profit by Location")
plt.xlabel("Location")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quantity by Product chart
qty_by_product.plot(kind="bar")

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit Margin by Location chart
profit_margin_by_location.plot(kind="bar")

plt.title("Profit Margin by Location")
plt.xlabel("Location")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit Margin by Product chart
profit_margin_by_product.plot(kind="bar")

plt.title("Profit Margin by Product")
plt.xlabel("Product")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales vs Profit by Product
product_comparison = data.groupby("Product")[["Sales", "Profit"]].sum()

product_comparison.plot(kind="bar")

plt.title("Sales vs Profit by Product")
plt.xlabel("Product")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales vs Profit by Location
location_comparison = data.groupby("Location")[["Sales", "Profit"]].sum()

location_comparison.plot(kind="bar")

plt.title("Sales vs Profit by Location")
plt.xlabel("Location")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quantity Sold by Location
quantity_by_location = data.groupby("Location")["Qty"].sum()

quantity_by_location.plot(kind="bar")

plt.title("Quantity Sold by Location")
plt.xlabel("Location")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by Year
sales_by_year.plot(kind="bar")

plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Profit by Year
profit_by_year = data.groupby(data["Date"].dt.year)["Profit"].sum()

profit_by_year.plot(kind="bar")

plt.title("Profit by Year")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Quantity Sold by Year
quantity_by_year = data.groupby(data["Date"].dt.year)["Qty"].sum()

quantity_by_year.plot(kind="bar")

plt.title("Quantity Sold by Year")
plt.xlabel("Year")
plt.ylabel("Quantity")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Sales by Month
sales_by_month.plot(kind="bar")

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(range(12), [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
], rotation=45)

plt.tight_layout()
plt.show()

# Profit by Month
profit_by_month = data.groupby(data["Date"].dt.month)["Profit"].sum()

profit_by_month.plot(kind="bar")

plt.title("Profit by Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(range(12), [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
], rotation=45)

plt.tight_layout()
plt.show()

# Sales Distribution by Product
sales_by_product.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales Distribution by Product")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Profit Distribution by Product
profit_by_product.plot(kind="pie", autopct="%1.1f%%")

plt.title("Profit Distribution by Product")
plt.ylabel("")
plt.tight_layout()
plt.show()