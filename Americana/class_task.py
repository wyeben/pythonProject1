while True:
    try:
        num1, num2 = eval(input("enter two numbers seperated by comma:"))
        result = num1 / num2
        print(result)
    except SyntaxError:
        print("put a valid number seperated by ,")
    except ZeroDivisionError:
        print("you cannot divide")
    else:
        print("good")
        break
    finally:
        print("bad")
        continue
