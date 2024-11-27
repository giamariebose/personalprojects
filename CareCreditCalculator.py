#import pandas as pd

def calculate_payments(df):
    """
    Calculates payments due for multiple accounts.

    Args:
        df (pd.DataFrame): DataFrame with columns 'account_id', 'balance', 'interest_rate', and 'payment_due_date'.

    Returns:
        pd.DataFrame: DataFrame with 'account_id' and 'payment_due' columns.
    """

import datetime
from datetime import timedelta

def get_date_input():
    while True:
        try:
            date_str = input("Enter a date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            return date
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")

nextduedate = get_date_input()
print("Next Due date:", nextduedate)
duedate2 = nextduedate + nextduedate.timedelta(days=30)
print("Due Date 2:", duedate2)

if __name__ == "__main__":
    # Sample data
    data = {
        'account_id': [1, 2, 3],
        'balance': [1000, 500, 2000],
        'payment_due_date': ['2024-12-15', '2024-12-20', '2024-12-10']
    }
    df = pd.DataFrame(data)

    # Calculate payments
    payments_df = calculate_payments(df)

    print(payments_df)