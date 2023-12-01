import pandas as pd
import matplotlib.pyplot as plt

# Reload the Excel file to extract the specific rows for the fourth group
file_path = 'E:/大四第一段/數學建模比賽/支撐材料/yin.xlsx'
data_full = pd.read_excel(file_path)

# Reload the Excel file to extract the specific rows for the fourth group
data_group_4 = pd.read_excel(file_path, skiprows=12, nrows=3)

# Clean the data to remove any NaN values that may affect the plotting
# Dropping the 'Cumulative Return' column to have only the days and returns
data_group_4_cleaned = data_group_4.dropna(axis=1).drop('Cumulative Return', axis=1)

# Getting the days for the x-axis (which are the column names of the dataframe)
# We filter out the columns where the 'Optimized' row (which is now the first row after skipping rows) is NaN
days_group_4 = [day for day in data_group_4_cleaned.columns if not pd.isna(data_group_4_cleaned.iloc[0][day])]

# Extracting the 'Optimized' and 'Non-optimized' returns for plotting
optimized_returns_group_4 = data_group_4_cleaned.iloc[0].dropna()
non_optimized_returns_group_4 = data_group_4_cleaned.iloc[1].dropna()

# Plotting the data for the fourth group
plt.figure(figsize=(14, 7))
plt.plot(days_group_4, optimized_returns_group_4, label='Optimized', marker='o', color='blue')
plt.plot(days_group_4, non_optimized_returns_group_4, label='Non-optimized', marker='s', color='green')

# Adding titles and labels
plt.title('Cumulative Return Over Time (Group 4)')
plt.xlabel('Time (Days)')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)

# We only label specific days on the x-axis as per the instruction
xticks = [day for day in days_group_4 if day in ['Day1', 'Day11', 'Day21', 'Day31', 'Day41', 'Day51', 'Day61', 'Day71', 'Day81']]
plt.xticks(ticks=xticks, labels=xticks, rotation=45)

plt.tight_layout()
plt.show()
