def calculate_ticket_price(age):
    if age < 6:
        return "Too young to ride!"
    elif age < 12:
        return "Ticket Price: ₦100"
    elif age <= 20:
        return "Ticket Price: ₦200"
    else:
        return "Ticket Price: ₦250"


def roller_coaster_game():
    print("Welcome to the Roller Coaster Game!")
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age <= 0:
                print("Invalid age. Please enter a valid age.")
            else:
                price_message = calculate_ticket_price(age)
                print(price_message)
                break
        except ValueError:
            print("Invalid input. Please enter a valid age as a number.")


roller_coaster_game()
