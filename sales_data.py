import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("DataFrame的前5行:")
print(df.head())

sales_series = df["Sales"]
print("\nSales的Series:")
print(sales_series)

total_sales = df.groupby("Date")["Sales"].sum().reset_index()
total_sales.columns = ["Date","Total Sales"]
print("\n每天的總銷售額：")
print(total_sales)

plt.figure(figsize=(10,5))
plt.plot(total_sales["Date"],total_sales["Total Sales"],marker = "o")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid()
plt.tight_layout()
plt.show()



