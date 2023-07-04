total_miles = 0
total_gallons = 0

miles = float(input("Enter miles driven (or -1 to exit): "))

while miles != -1:
    gallons = float(input("Enter gallons used: "))

    mpg = miles / gallons
    print("Miles per gallon: {:.2f}".format(mpg))

    total_miles += miles
    total_gallons += gallons

    miles = float(input("Enter miles driven (or -1 to exit): "))

if total_gallons != 0:
    combined_mpg = total_miles / total_gallons
    print("The overall average miles/gallon was: {:.2f}".format(combined_mpg))
else:
    print("No data entered.")