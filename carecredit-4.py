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
from dateutil.relativedelta import relativedelta
import pandas as pd


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
##MIGHT REMOVE AS COULDN"T BUILD INTO LOOP
def calculate_next_due_date(calc_nextduedate, end_date):
    print(f"Next Due Date: {calc_nextduedate}")
    due_day = calc_nextduedate.day 

    #move to next month
    next_month = calc_nextduedate.month % 12 + 1
    next_year = calc_nextduedate.year + (calc_nextduedate.month // 12)
    ##testing date here
    try:
        calc_nextduedate = date(next_year, next_month, due_day)
    except ValueError:
        # If the day is invalid, adjust to the last day of the month
        last_day = calendar.monthrange(next_year, next_month)[1]
        calc_nextduedate = date(next_year, next_month, due_day)     


##prompt for csv file with windows explorer
##current csv has headers NextDueDate, PromoExpiration, PromoBalance
root = tk.Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename(title="Select csv that contains promo information")

if file_path:
    print("Selected file:", file_path)

##prompt for folder to store exports
dialog_title = "Select a Folder for Results"
export_path = filedialog.askdirectory(title=dialog_title)

##declare overall csv export
export_csv_all = export_path + "/ALL_Promos.csv"
print(f"csv of all will be exported to {export_csv_all}")
final_csv_out = export_path + "/ALL_Promos_final.csv"

##create overall csv export file with headers
headers_export = ["PromoID", "DueDate", "MonthlyPayment", "RunningTotal"]
   
# Create a CSV file and write the headers for promo specific csv
with open(export_csv_all, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers_export)
    writer.writeheader()


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

   ##set variable for temporary file name and write headers
   promoIDstr = str(promoID)
   promotempexport = export_path+"/tempdata_promoID"+promoIDstr+".csv"
   #print(f"temp files will export to {promotempexport}")
   headers_export = ["PromoID", "DueDate", "MonthlyPayment", "RunningTotal"]
   
   # Create a CSV file and write the headers for promo specific csv
   with open(promotempexport, mode="w", newline="") as file:
       writer = csv.DictWriter(file, fieldnames=headers_export)
       writer.writeheader()

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
   thirtysixmonthsout = nextduedate + relativedelta(months=36)
   ##temp print for testing
   print(f"36 months out {thirtysixmonthsout}")
   #next36payments = calculate_next_due_date(nextduedate, thirtysixmonthsout)
   #loop here for number of payments remaining
   previouslypaid = int("0")
   for i in range(promopaymentsremaining):
    runningtotal = promomonthlypaymentsround+previouslypaid
    previouslypaid = runningtotal
    # print(f"due date: {autonextduedatedate}")
    # print(f"monthly payment due: {monthlypayment}")
    # print(f"total paid to date is: {runningtotal}")    

    # move to next month
    next_month = nextduedate.month % 12 + 1
    next_year = nextduedate.year + (nextduedate.month // 12)
    ##testing date here
    try:
        nextduedate = date(next_year, next_month, nextdueday)
    except ValueError:
        # If the day is invalid, adjust to the last day of the month
        last_day = calendar.monthrange(next_year, next_month)[1]
        nextduedate = date(next_year, next_month, last_day) 
    print("- - - - - - - - - - - - - - - - - - - - -- - --")
    print(f"Next Due Date: {nextduedate}")
    print(f"Monthly Payment: {promomonthlypaymentsround}")
    print(f"Running Total: {previouslypaid:.2f}")

    ##store data in dic
    promorowforcsv = [promoID, nextduedate, promomonthlypaymentsround, previouslypaid]

    ##write rows to promo specific temp csv
    with open(promotempexport, mode="a", newline="") as file:
        #writer = csv.DictWriter(file, fieldnames=headers_export)
        writer = csv.writer(file)
        writer.writerow(promorowforcsv)
    
    ##write rows to promo csv of all
    with open(export_csv_all, mode="a", newline="") as file:
        #writer = csv.DictWriter(file, fieldnames=headers_export)
        writer = csv.writer(file)
        writer.writerow(promorowforcsv)
    
 

   ##increase promo ID number before looping again.
   promoID += 1

##use csv to import and calculate further

allpromosdf = pd.read_csv(export_csv_all)

# Pivot the data so that each PromoID becomes its own set of columns
pivoted = allpromosdf.pivot(index="DueDate", columns="PromoID", values=["MonthlyPayment", "RunningTotal"])

# Flatten the MultiIndex columns
pivoted.columns = [f"{col[0]}_{col[1]}" for col in pivoted.columns]

# Reset the index to make DueDate a column again
pivoted.reset_index(inplace=True)

# Add total columns for MonthlyPayment and RunningTotal
pivoted["TotalMonthlyPayment"] = pivoted.filter(like="MonthlyPayment").sum(axis=1)
##this one doesn't total right
#pivoted["TotalRunningTotal"] = pivoted.filter(like="RunningTotal").sum(axis=1)
pivoted["RunningTotal"] = pivoted["TotalMonthlyPayment"].cumsum()

# Save the final table to a CSV file
output_file = "promotion_summary_pivoted.csv"
pivoted.to_csv(final_csv_out, index=False)

print(f"Pivoted summary file saved to {final_csv_out}")

#print(pivoted)

##then delete temp csvs?
##display results?

## OR 

## ADD: combine output from previous on matching dates to a table with columns
##       - Next Due Date
##       - PromoID monthly payment
##       - Running total paid
##       - all promos monthly payment
##       - all promos running total
   