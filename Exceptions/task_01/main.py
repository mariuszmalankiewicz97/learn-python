try:
    number_1 = float(input("Give me the first number: "))
    number_2 = float(input("Give me the secound number: "))
    result = number_1 / number_2
except ValueError:
    print("Use format: int, float")
except TypeError:
    print("Input must be a number")
except ZeroDivisionError:
    print("Cannot be divided by zero")
else:
    print(f"{number_1} / {number_2} = {result}")
finally:
    print("Program end")
