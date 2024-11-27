# import module
from tabulate import tabulate
from datetime import datetime, date, timedelta
import re

start_date = date.today()
print("startdate is ")
print(start_date)

##testing to see if I can get the date and break it out the way I want
while True:
    try:
        autodatenextdue = input("enter next payment due date MM-DD-YYYY:")
        pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
        # Check if the input matches the pattern
        if re.match(pattern, autodatenextdue):
            print(f"The date {autodatenextdue} is valid.")
            break
        else:
            print("Invalid date format. Please enter a date in MM-DD-YYYY format.")
    except ValueError:
            print("Invalid input. please enter valid day as number") 

##less repetitive split
autonextduesplit = autodatenextdue.split("-")
automonthdue = int(autonextduesplit[0])
autodaydue = int(autonextduesplit[1])
autoyeardue = int(autonextduesplit[2]) 
autonextduedatedate = date(autoyeardue, automonthdue, autodaydue)

##the following splits successfully, above attempting to clean up
#automonthdue = autodatenextdue.split("-")[0]
#autodaydue = autodatenextdue.split("-")[1]
#autoyeardue = autodatenextdue.split("-")[2]
print(f"monthly payment due on the {autodaydue} of the month")
print(f"monthly payment due in {automonthdue}")
print(f"monthly payment due in {autoyeardue}")
print(f"promo expires on date {autonextduedatedate}")

##the below works to gather a broken out date for expiration.
#while True:
#    try:
#        monthlydaydue = int(input("On what day of the month is payment due?"))
#        if 1 <= monthlydaydue <= 28:
#            break  # Valid input; exit the loop
#        else:
#            print("This calculator can only calculate for due dates between 1 and 28, please enter 28 if due date is usually later.")    
#            
#    except ValueError:
#        print("Invalid input. please enter valid day as number") 
#
#print("payments are due on the " + str(monthlydaydue) + " of the month")
#

##will need to add a counter above for number of promos, then can add fxn/loop for each promo

while True:
    try:
        autopromoexpirationdate = input("Enter promo expiration date MM-DD-YYYY:")
        pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
        # Check if the input matches the pattern
        if re.match(pattern, autopromoexpirationdate):
            print(f"The date {autopromoexpirationdate} is valid.")
            break
        else:
            print("Invalid date format. Please enter a date in MM-DD-YYYY format.")
    except ValueError:
            print("Invalid input. please enter valid day as number") 

autopromoexpirationdatesplit = autopromoexpirationdate.split("-")
autopromoexpmonth = int(autopromoexpirationdatesplit[0])
autopromoexpday = int(autopromoexpirationdatesplit[1])
autopromoexpyear = int(autopromoexpirationdatesplit[2]) 
autopromoexpdatedate = date(autopromoexpyear, autopromoexpmonth, autopromoexpday)

##the following splits successfully, above attempting to clean up
#automonthdue = autodatenextdue.split("-")[0]
#autodaydue = autodatenextdue.split("-")[1]
#autoyeardue = autodatenextdue.split("-")[2]
print(f"promo expires on the {autopromoexpday} of the month")
print(f"promo expires in {autopromoexpmonth}")
print(f"promo expires in {autopromoexpyear}")
print(f"promo expires on date {autopromoexpdatedate}")



##original promo expiration works, working to improve above
#while True:
#    try:
#        promoexpirationyear = int(input("Enter promo expiration year (YYYY): "))
#        break #exit loop if the input is valid
#    except ValueError:
#        print("Invalid input. please enter valid year as number")
#
#while True:
#    try:
#        promoexpirationmonth = int(input("Enter promo expiration month (MM): "))
#        break #exit loop if the input is valid
#    except ValueError:
#        print("Invalid input. please enter valid year as number")
#
#while True:
#    try:
#        promoexpirationday = int(input("Enter promo expiration day (DD): "))
#        if 1 <= promoexpirationday <= 31:
#            break  # Valid input; exit the loop
#        else:
#            print("Invalid input. Please enter a number between 1 and 31.")
#    except ValueError:
#        print("Invalid input. please enter valid year as number")
#
#
#promoexpirationdate = date(promoexpirationyear, promoexpirationmonth, promoexpirationday)
#print("promo expires:")
#print(promoexpirationdate)

##IF DUE DATE IS LATER THAN 28, THIS MAY BE OFF FOR SHORTER MONTHS OR FEBRUARY/LEAP YEAR
##TESTING WITH EARLY DUE DATES
def count_months_with_due_date(due_day, end_date):
    count = 0
    #current_date = date.today().replace(day=1)  # Start from the 1st of the current month
    current_date = date.today()

    while current_date <= end_date:
        try:
            # Set the day to the due day for the current month
            due_date = current_date.replace(day=due_day)
            if due_date <= end_date:
                count += 1
        except ValueError:
            # Skip months where the due day doesn't exist (e.g., February 30)
            ##CONSIDER ADDING CONVERSION OF DUE DAY TO 28 IF DAY IS 29/30/31
            pass
        
        # Move to the first day of the next month
        next_month = current_date.month % 12 + 1
        next_year = current_date.year + (current_date.month // 12)
        current_date = current_date.replace(year=next_year, month=next_month, day=1)
    
    return count

try:
    result = count_months_with_due_date(autodaydue, autopromoexpdatedate)
    print(f"The number of months with a {autodaydue} before {autopromoexpdatedate} is: {result}")
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

print("balance due is: $",balancedue," and the full payment is due by ",autopromoexpdatedate)

monthlypayment = balancedue/result
print("monthly payments required for this balance $",monthlypayment)

##does the current month have a due date that hasn't passed?
##if date has passed
##then start listing month/year from next month with monthly payment and running total until number of months until expiration have passed
##if date has not passed
##then start listing month/year from this month with monthly payment and running total until number of months until expiration have passed