# Compound Interest Calculator
principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the Principal amount: ").replace(",", ""))
    if principal <= 0:
        print("Principal amount must be greater than zero.")

while rate <= 0:
    rate = float(input("Enter the annual interest rate (%): "))
    if rate <= 0:
        print("Interest rate must be greater than zero.")

while time <= 0:
    time = int(input("Enter Time in years: "))
    if time <= 0:
        print("Time period must be greater than zero.")
total = principal * pow ((1+rate/100), time)
print(f"Your total amount after {time} years is ₹{total:,.2f}")
