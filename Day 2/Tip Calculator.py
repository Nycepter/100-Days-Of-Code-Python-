BillTotal = float(input("What is the bill total? $"))
Percentage = float(input("What percentage would you like to tip? "))
SplitWay = int(input("How many people are splitting the bill? "))
BillWithTip = float(BillTotal + (BillTotal * (Percentage / 100)))
EndTotal = round(BillWithTip / SplitWay, 2)

print(f"Each person should pay: ${EndTotal}")
