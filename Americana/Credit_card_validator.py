def validate_card(card_number):
    card_number = card_number.replace(' ', '').replace('-', '')

    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 16:
        return False

    total = 0
    reverse_digits = card_number[::-1]
    is_second_digit = False

    for digit in reverse_digits:
        current_digit = int(digit)
        if is_second_digit:
            current_digit *= 2
            if current_digit > 9:
                current_digit -= 9
        total += current_digit
        is_second_digit = not is_second_digit

    return total % 10 == 0


def get_card_type(card_number):
    if card_number.startswith('4'):
        return 'Visa'
    elif card_number.startswith('5'):
        return 'MasterCard'
    elif card_number.startswith('37'):
        return 'American Express'
    elif card_number.startswith('6'):
        return 'Discover'
    else:
        return 'Unknown'


def credit_card_validator_test():
    card_number = input("Enter a credit card number: ")

    if validate_card(card_number):
        card_type = get_card_type(card_number)
        if card_type != 'Unknown':
            print(f"Valid {card_type} credit card number.")
        else:
            print("Valid credit card number of unknown type.")
    else:
        print("Invalid credit card number.")


if __name__ == "__main__":
    credit_card_validator_test()
