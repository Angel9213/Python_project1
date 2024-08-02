import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_data.csv")

print("DataFrame的頭5行：")
print(df.head())

salary = df["Salary"]
print("\nSalary的Series：")
print(salary)

average_salary = df.groupby("Department")["Salary"].mean().reset_index()
average_salary.columns = ["Department", "Salary"]
print("\n每個部門的平均薪水：")
print(average_salary)

plt.figure(figsize=(10,5))
plt.bar(average_salary["Department"],average_salary["Salary"])
plt.title("Department Average Salary")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.grid()
plt.tight_layout()
plt.show()
