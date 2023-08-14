calculate_total_price_with_vat = lambda: ((lambda p, v: p + p * v / 100 if p > 0 and v > 0 else "")
                                          (int(input("Enter the price of the item: ")),
                                           int(input("Enter the VAT percentage: "))))

while True:
    try:
        total_price = calculate_total_price_with_vat()
        print(f"The total price including VAT is: {total_price:.2f}")
        break
    except ValueError:
        print("Invalid input. Please enter valid values.")