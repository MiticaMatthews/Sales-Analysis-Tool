
import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt

total_sales = 0
months = []
sales = []
expenditure = []
profits = []

# Open and read CSV file
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for i in spreadsheet:
        total_sales += int(i['sales'])
        months.append(i['month'])
        sales.append(int(i['sales']))
        expenditure.append(int(i['expenditure']))
        profits.append(int(i['sales']) - int(i['expenditure']))

    # Create a DataFrame using sales data
    new_spreadsheet = {
    'Month': months,
    'Sales' : sales,
    'Expenditure' : expenditure,
    'Profit' : profits
}
    # Calculate percentage change of monthly sales & add data to new column
    df = pd.DataFrame(new_spreadsheet)
    df['Percentage Change'] = df['Sales'].pct_change() * 100
    df['Percentage Change'] = df['Percentage Change'].round(2) # Round float to 2 decimal places

# Calculate statistics
average = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)
highest = max(sales)
lowest = min(sales)

# Create a separate DataFrame for the statistics
statistics_data = {
    'Month': ['Total Sales', 'Mean', 'Median', 'Mode', 'Highest Sales', 'Lowest Sales'],
    'Sales': [total_sales, average, median, mode, highest, lowest],
    'Expenditure': [''] * 6,
    'Profit': [''] * 6,
    'Percentage Change': [''] * 6


}
statistics_df = pd.DataFrame(statistics_data)

# Combine sales and statistics DataFrames
combined_df = pd.concat([df, statistics_df], ignore_index=True)
combined_df['Sales'] = combined_df['Sales'].round().astype(int)

# Write final DataFrame to a new CSV file
combined_df.to_csv('monthly_sales_and_stats.csv', index=False)

# Print final DataFrame
print(combined_df)

# Create a bar chart for Monthly Sales:
plt.bar(months, sales, color = "pink")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

# Create a line chart for Sales & Expenditure:
plt.plot(months, sales, label = "Sales", color = "hotpink")
plt.plot(months, expenditure, label = "Expenditure", color = "lightgreen")
plt.xlabel("Months")
plt.ylabel("GBP")
plt.title("Sales and Expenditure over 12 Months")
plt.legend() # Legend to differentiate lines in chart
plt.show()