from datetime import date
import calendar

# Get today's date
today = date.today()

# Initialize a list to store month names and days
month_data = []

# Loop through the next 6 months
for i in range(6):
    # Calculate the target month and year
    target_month = (today.month + i - 1) % 12 + 1
    target_year = today.year + (today.month + i - 1) // 12
    
    # Get the number of days in the month
    num_days = calendar.monthrange(target_year, target_month)[1]
    
    # Store the month name and number of days as a tuple
    month_name = calendar.month_name[target_month]
    month_data.append((month_name, num_days))

# Print the data as a table
print(f"{'Month':<15}{'Days in Month':<15}")
print("-" * 30)
for month_name, num_days in month_data:
    print(f"{month_name:<15}{num_days:<15}")
