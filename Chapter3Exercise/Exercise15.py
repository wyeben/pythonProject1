def calculate_e(num_terms):
    e = 1
    factorial = 1

    for i in range(1, num_terms + 1):
        factorial *= i
        e += 1 / factorial

    return e

num_terms = 10
e_estimate = calculate_e(num_terms)

print("Estimating the value of e using", num_terms, "terms:")
print("e ≈", e_estimate)