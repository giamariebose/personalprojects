from datetime import date

class promos:
    balancedue = float(0.00)
    promoname = "first promo"
    duedate = date(2024, 11, 28)
    monthlypayment = float(75.24)
    runningtotal = float(170.51)

promo1 = promos()
print("Promo Name:")
print(promo1.promoname)
print("Due Date:")
print(promo1.duedate)
print("monthly payment:")
print(promo1.monthlypayment)

