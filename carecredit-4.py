##attempting to use csv import


##import modules
import csv
import tkinter as tk
from tkinter import filedialog

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
  print(header)
  rows = []
  for row in csv_reader:
    rows.append(row)
print(rows)
csvfile.close()
  
##count number of rows in rows
promocount = len(rows)
print(f"number of promos: {promocount}")

