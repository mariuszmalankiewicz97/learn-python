numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Give me an index: "))
    print(numbers[index])
except ValueError:
    print("Number must have format int")
except IndexError:
    print(f"Give integer number from 0 to {len(numbers) - 1}")
else:
    print("Index is correct")
finally:
    print("Program end")
