##attempting to use csv import


##import modules
import csv
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate
from datetime import datetime, date, timedelta
import re
from tabulate import tabulate
import calendar
import math

##Define Formats and Functions

#FORMAT: Currency
def format_currency(amount):
    return "${:,.2f}".format(amount)

##FUNCTION: date test for correcting days out of range:
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

##FUNCTION: rounding up
def round_up_to_nearest_hundredth(x):
    return math.ceil(x * 100) / 100

##FUNCTION: count months with due date
def count_months_with_due_date(due_day, end_date):
    count = 0
    #current_date = date.today().replace(day=1)  # Start from the 1st of the current month
    current_date = nextduedate

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

##FUNCTION: move to next due month with checking for valid date
def calculate_next_due_date(due_day, end_date):

    #move to next month
    next_month = nextduedate.month % 12 + 1
    next_year = nextduedate.year + (autonextduedatedate.month // 12)
    ##testing date here
    try:
        nextduedate = date(next_year, next_month, nextdueday)
    except ValueError:
        # If the day is invalid, adjust to the last day of the month
        last_day = calendar.monthrange(next_year, next_month)[1]
        nextduedate = date(next_year, next_month, last_day)     


##prompt for csv file with windows explorer
##current csv has headers NextDueDate, PromoExpiration, PromoBalance
root = tk.Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename()

if file_path:
    print("Selected file:", file_path)

# Open the CSV file in read mode
with open(file_path, 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile)
  header = next(csv_reader)
  ##printing used for testing
  #print(header)
  rows = []
  for row in csv_reader:
    rows.append(row)
##printing used for testing    
#print(rows)
csvfile.close()
  
##count number of rows in rows
promocount = len(rows)
print(f"number of promos: {promocount}")

#declare first promo ID, will be incremented in next loop
promoID = int('1')

for promo in rows:
   print("_________________________________________________")
   ## set variables for duedate, expiration, amountfinanced
   nextduesplit = promo[0].split("/")
   nextduemonth = int(nextduesplit[0])
   nextdueday = int(nextduesplit[1])
   nextdueyear = int(nextduesplit[2])
   nextduedate = date(nextdueyear, nextduemonth, nextdueday)
   promoexpsplit = promo[1].split("/")
   promoexpmonth = int(promoexpsplit[0])
   promoexpday = int(promoexpsplit[1])
   promoexpyear = int(promoexpsplit[2])
   promoexpdate = date(promoexpyear, promoexpmonth, promoexpday)
   promoamountfinanced = float(promo[2])

   ##print promo information
   print(f"Promo ID: {promoID}")
   print(f"Next Due Date: {nextduedate}")
   print(f"Promo Expiration: {promoexpdate}")
   ##note to self, look here to display two decimal places
   print(f"Amount Financed: ${promoamountfinanced:.2f}")

   ## calculate monthly payments remaining
   promopaymentsremaining = count_months_with_due_date(nextdueday, promoexpdate)
   print(f"Number of Due Dates before Expiration: {promopaymentsremaining}")
   
   ## calculate monthly payments
   promomonthlypayments = promoamountfinanced / promopaymentsremaining
   promomonthlypaymentsround = round_up_to_nearest_hundredth(promomonthlypayments)
   print(f"Monthly Payment Required: ${promomonthlypaymentsround}")

   ##ADD: calculate upcoming due dates and store in a temporary array for next 36 months?
   ##if so, end date is nextduedate + 36 months
        ##ADD: split day out of next payment due
   #loop here for number of payments remaining
   #nextnextduedate = calculate_next_due_date(due_day, end_date)
   ##ADD: define previously paid as 0

   ##ADD:  loop thru array

       ##ADD: calculate previously paid+monthly payment
       ##ADD: calculate remaining balance as balancedue - previously paid
       ##ADD:  note: using previously paid after adding current month payment so it includes both at this point

   
   ##dump these out line by line to a temp csv

   ##increase promo ID number before looping again.
   promoID += 1

##use temp csv to import and calculate further
##then dump out to final csv
##then delete temp csv
##display results?