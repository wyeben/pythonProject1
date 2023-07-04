import math

def calculate_pi(num_terms):
    pi = 0
    sign = 1

    for i in range(1, num_terms * 2, 2):
        pi += sign * (4 / i)
        sign *= -1

    return pi

target_values = [3.14, 3.141, 3.1415, 3.14159]

print("Approximating π using infinite series:")
print("")

for target in target_values:
    num_terms = 1
    current_pi = calculate_pi(num_terms)

    while current_pi < target:
        num_terms += 1
        current_pi = calculate_pi(num_terms)

    print("To reach", target, "you need", num_terms, "terms.")