



# import module
from tabulate import tabulate
from datetime import datetime, date, timedelta


# assign data
mydata = [
    ['a', 'b', 'c'],
      [date(2025, 5, 15), date(2025, 11, 5), date(2025, 11, 15)],
      [500, 1600, 3500]
]


# display table
print(tabulate(mydata))

##
start_date = date.today()
print("startdate is ")
print(start_date)
##end date for testing
#end_date = date(2024, 5, 15) 
#print("endate is " )
#print(end_date)



def get_date_input():
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date_obj = date.fromisoformat(date_str)
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

nextduedate = get_date_input()
print("Next Due date:", nextduedate)

monthlyduedate = nextduedate.day
print("monthly payments due on:", monthlyduedate)

def count_months_with_second(start_date, end_date):
    count = 0
    current_date = start_date.replace(day=1)  # Start at the first day of the month
    
    while current_date <= end_date:
        second_of_month = current_date.replace(day=2)
        if second_of_month >= start_date and second_of_month <= end_date:
            count += 1
        # Move to the first day of the next month
        next_month = current_date.month % 12 + 1
        next_year = current_date.year + (current_date.month // 12)
        current_date = current_date.replace(year=next_year, month=next_month)
    
    return count

# Example usage
start_date = date.today()
end_date = date(2025, 5, 15)

result = count_months_with_second(start_date, end_date)
print(f"Number of months with a 2nd between {start_date} and {end_date}: {result}")
