import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Internship work/5th task/Finance.xlsx'
df = pd.read_excel(file_path)


print("First 5 rows of the dataset:\n", df.head())
print("\nLast 5 rows of the dataset:\n", df.tail())
print("\nData info:\n")
df.info()

print("\nMissing values:\n", df.isnull().sum())


df['Year Order'] = pd.to_datetime(df['Order Date'], errors='coerce').dt.year


df.dropna(subset=['Year Order'], inplace=True)


year_counts = df['Year Order'].value_counts().sort_index()


plt.figure(figsize=(10, 6))
year_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Orders per Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


revenue_by_region = df.groupby('Region')['Total Revenue'].sum()
plt.figure(figsize=(8, 8))
plt.pie(revenue_by_region, labels=revenue_by_region.index, autopct='%1.1f%%', 
        startangle=140, colors=plt.cm.Paired.colors, wedgeprops={'edgecolor': 'black'})
plt.title('Total Revenue by Region', fontsize=16)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
plt.scatter(year_counts.index, year_counts.values, marker='o', color='blue', s=100)
plt.gca().set_facecolor('whitesmoke')
plt.title('Number of Orders per Year (Dot Graph)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(year_counts.index)
plt.tight_layout()
plt.show()
