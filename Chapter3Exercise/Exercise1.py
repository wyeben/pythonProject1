passes = 0
failures = 0

while True:
    result = int(input("Enter result (1 = pass, 2 = fail): "))

    if result == 1:
        passes += 1
    elif result == 2:
        failures += 1
    else:
        print("Invalid input. Please enter either 1 or 2.")
        continue

    print("Passes:", passes)
    print("Failures:", failures)
    if passes > 8:
      print('bonus to instructor')
      break