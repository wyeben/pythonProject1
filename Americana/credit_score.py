def calculate_discount(price, credit_score):
    if credit_score == "good":
        discount = 0.1
    else:
        discount = 0

    discount_amount = price * discount
    discounted_price = price - discount_amount
    return discounted_price


def calculate_down_payment(price, credit_score):
    if credit_score == "good":
        down_payment_percentage = 0.1
    else:
        down_payment_percentage = 0.25

    down_payment_amount = price * down_payment_percentage
    return down_payment_amount



item_price = 1000
credit = "good"

discounted_price = calculate_discount(item_price, credit)
down_payment = calculate_down_payment(item_price, credit)

print("Discounted price: naira", discounted_price)
print("Down payment: naira", down_payment)