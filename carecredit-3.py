# import module
from tabulate import tabulate
from datetime import datetime, date, timedelta

start_date = date.today()
print("startdate is ")
print(start_date)

while True:
    try:
        monthlydaydue = int(input("On what day of the month is payment due?"))
        if 1 <= monthlydaydue <= 28:
            break  # Valid input; exit the loop
        else:
            print("This calculator can only calculate for due dates between 1 and 28, please enter 28 if due date is usually later.")    
            
    except ValueError:
        print("Invalid input. please enter valid day as number") 

print("payments are due on the " + str(monthlydaydue) + " of the month")

while True:
    try:
        promoexpirationyear = int(input("Enter promo expiration year (YYYY): "))
        break #exit loop if the input is valid
    except ValueError:
        print("Invalid input. please enter valid year as number")

while True:
    try:
        promoexpirationmonth = int(input("Enter promo expiration month (MM): "))
        break #exit loop if the input is valid
    except ValueError:
        print("Invalid input. please enter valid year as number")

while True:
    try:
        promoexpirationday = int(input("Enter promo expiration day (DD): "))
        if 1 <= promoexpirationday <= 31:
            break  # Valid input; exit the loop
        else:
            print("Invalid input. Please enter a number between 1 and 31.")
    except ValueError:
        print("Invalid input. please enter valid year as number")


promoexpirationdate = date(promoexpirationyear, promoexpirationmonth, promoexpirationday)
print("promo expires:")
print(promoexpirationdate)

##IF DUE DATE IS LATER THAN 28, THIS MAY BE OFF FOR SHORTER MONTHS OR FEBRUARY/LEAP YEAR
##TESTING WITH EARLY DUE DATES
def count_months_with_due_date(due_day, end_date):
    count = 0
    current_date = date.today().replace(day=1)  # Start from the 1st of the current month
    
    while current_date <= end_date:
        try:
            # Set the day to the due day for the current month
            due_date = current_date.replace(day=due_day)
            if due_date <= end_date:
                count += 1
        except ValueError:
            # Skip months where the due day doesn't exist (e.g., February 30)
            pass
        
        # Move to the first day of the next month
        next_month = current_date.month % 12 + 1
        next_year = current_date.year + (current_date.month // 12)
        current_date = current_date.replace(year=next_year, month=next_month, day=1)
    
    return count

try:
    result = count_months_with_due_date(monthlydaydue, promoexpirationdate)
    print(f"The number of months with a {monthlydaydue} before {promoexpirationdate} is: {result}")
except ValueError as e:
    print(f"Invalid input: {e}")

##at this point the following variables are key
## result is the count of months with the due date between current date and expiration
## promoexpirationdate is the expiration date of the promo

while True:
    try:
        balancedue = float(input("Enter balancedue: "))
        break #exit loop if the input is valid
    except ValueError:
        print("Invalid input. please enter valid year as number")

print("balance due is: $",balancedue," and the full payment is due by ",promoexpirationdate)

monthlypayment = balancedue/result
print("monthly payments required for this balance $",monthlypayment)

##does the current month have a due date that hasn't passed?
##if date has passed
##then start listing month/year from next month with monthly payment and running total until number of months until expiration have passed
##if date has not passed
##then start listing month/year from this month with monthly payment and running total until number of months until expiration have passed