import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'E:/大四第一段/數學建模比賽/支撐材料/yin_day.xlsx'
data_full = pd.read_excel(file_path)

# Extract the specific rows for the four groups and clean the data
groups_data = [
    data_full.iloc[0:3, :].dropna(axis=1, how='all'),  # 1st group: rows 1-3
    data_full.iloc[4:7, :].dropna(axis=1, how='all'),  # 2nd group: rows 5-7
    data_full.iloc[8:11, :].dropna(axis=1, how='all'), # 3rd group: rows 9-11
]

# Function to plot each group
def plot_group(data, group_idx, title):
    # Set the plot size
    plt.figure(figsize=(14, 7))

    # Extract data for plotting
    dates = data.columns[1:]  # Skipping the 'Cumulative Return' column
    optimized_returns = data.iloc[0, 1:].values  # Optimized data
    non_optimized_returns = data.iloc[1, 1:].values  # Non-optimized data

    # Plotting the data
    plt.plot(dates, optimized_returns, label='Optimized', marker='o', color='blue')
    plt.plot(dates, non_optimized_returns, label='Non-optimized', marker='s', color='green')

    # Adding titles and labels
    plt.title(f'{title} (Group {group_idx})')
    plt.xlabel('Time (Days)')
    plt.ylabel('Cumulative Return')
    plt.legend()

    # Improving display
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjusts the plot to ensure everything fits without overlapping

    # Show the plot
    plt.show()

# Loop through each group and plot the data
for idx, group_data in enumerate(groups_data, start=1):
    plot_group(group_data, idx, "Cumulative Return Over Time")
