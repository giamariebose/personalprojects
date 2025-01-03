## NOTES
## depending on the amount and lenth of financing, rounding could have caused the payments to be under.
## to alleviate this, rounding was forced to round up. This can cause payments to be over by a few pennies.
## this should be negligible but errors on the side over overpaying by a few pennies rather than underpaying 
## to mitigate risk of underpaying and missing promo date by pennies, which could end up costing the full financing to be charged.
## in the long run, when down to the last few payments, should monitor expirations/balance closely regardless
## this tool is designed to be as exact as possible, but is not a guarantee.

##Next thoughts
## - change to use dictionary
## - since dic cannot have duplicate keys, create next 36 due dates and populate into a due dates dictionary
## - sub dictionary for monthly payment and running total
## - build calculations into functions, so that number of promos can be prompted and fxn run for each to store in subdic.
## - CORRECTED: Rounding down could have caused a minor underpayment, forcing round up
## - CORRECTED: Date calculations if due date is in last days of month. 
##              this fixes skipping due dates for months that don't have those days and calculating payments for those months

# import module
from tabulate import tabulate
from datetime import datetime, date, timedelta
import re
from tabulate import tabulate
import calendar
import math




# Initialize a list to store mdata
carecredit_data = []

#define currency format
def format_currency(amount):
    return "${:,.2f}".format(amount)

##define date test for correcting days out of range:
def adjust_date_to_last_day(input_date):
    try:
        # Try to use the input date as-is
        valid_date = input_date
        return valid_date
    except ValueError:
        # If the day is invalid, adjust to the last day of the month
        year = input_date.year
        month = input_date.month
        last_day = calendar.monthrange(year, month)[1]
        return date(year, month, last_day)

##define rounding up
def round_up_to_nearest_hundredth(x):
    return math.ceil(x * 100) / 100


#start_date = date.today()
#print("startdate is ")
#print(start_date)

##testing to see if I can get the date and break it out the way I want
while True:
    try:
        autodatenextdue = input("enter next payment due date MM-DD-YYYY:")
        pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
        # Check if the input matches the pattern
        if re.match(pattern, autodatenextdue):
            autonextduesplit = autodatenextdue.split("-")
            automonthdue = int(autonextduesplit[0])
            autodaydue = int(autonextduesplit[1])
            autoyeardue = int(autonextduesplit[2]) 
            autonextduedatedate = date(autoyeardue, automonthdue, autodaydue)
            ##option for making all dates 28 to catch months without a 29/30/31
            #if autodaydue > 28:
            #    autodaydue = 28
            #    autonextduedatedate = date(autoyeardue, automonthdue, autodaydue)
            #    print(f"Due date {autodaydue} is after the 28th, to handle months with less than 28 days, due dates will be shown as the 28th of the month")                
            print(f"The date {autonextduedatedate} is valid.")
            break
        else:
            print("Invalid date format. Please enter a date in MM-DD-YYYY format.")
    except ValueError:
            print("Invalid input. please enter valid day as number") 

##less repetitive split


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
    current_date = autonextduedatedate

    while current_date <= end_date:
        try:
            # Set the day to the due day for the current month
            try:
                due_date = current_date.replace(day=due_day)
            except ValueError:
                last_day = calendar.monthrange(next_year, next_month)[1]
                due_date = date(next_year, next_month, last_day)
            ##check if date is valid for month
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
## autopromoexpdatedate is the expiration date of the promo in date format

while True:
    try:
        balancedue = float(input("Enter balancedue: "))
        break #exit loop if the input is valid
    except ValueError:
        print("Invalid input. please enter balance due as number")

print("balance due is: $",balancedue," and the full payment is due by ",autopromoexpdatedate)

monthlypaymentfull = balancedue/result
#original rounding which can round down
#monthlypayment = round(balancedue/result,2)
monthlypayment = round_up_to_nearest_hundredth(monthlypaymentfull)
print("monthly payments required for this balance $",monthlypayment)



##then start listing month/year from this month with monthly payment and running total until number of months until expiration have passed
previouslypaid = int("0")
for i in range (result):
    runningtotal = monthlypayment+previouslypaid
    previouslypaid = runningtotal
 #   print(f"due date: {autonextduedatedate}")
 #   print(f"monthly payment due: {monthlypayment}")
 #   print(f"total paid to date is: {runningtotal}")    

    ##print table of data
    carecredit_data.append((autonextduedatedate, monthlypayment, runningtotal))

    #move to next month
    next_month = autonextduedatedate.month % 12 + 1
    next_year = autonextduedatedate.year + (autonextduedatedate.month // 12)
    ##testing date here
    try:
        autonextduedatedate = date(next_year, next_month, autodaydue)
    except ValueError:
        # If the day is invalid, adjust to the last day of the month
        last_day = calendar.monthrange(next_year, next_month)[1]
        autonextduedatedate = date(next_year, next_month, last_day)     

    #autonextduedatedate = autonextduedatedate.replace(year=next_year, month=next_month)
    

headers = ["Due Date", "Monthly Payment", "Running Total"]

print(tabulate(carecredit_data, headers=headers, tablefmt="grid", floatfmt=(".2f", ".2f", ".2f")))

#print(carecredit_data)

#for autonextduedatedate, monthlypayment, runningtotal in carecredit_data:
#    print(f"{autonextduedatedate:<15}{monthlypayment:<15}{runningtotal:<15}")
    
    ##next:
# get the data to store in an array and display as a table
#  build the promos into functions and add a prompt for number of promos and loop through
