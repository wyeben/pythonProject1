initial_amount = float(input("Enter the initial amount of money: "))

interest_rate = float(input("Enter the annual interest rate (in percentage): "))

interest_rate /= 100

amount = initial_amount
for year in range(1, 31):
    amount += amount * interest_rate
    print("Year", year, ": naira", round(amount, 2))