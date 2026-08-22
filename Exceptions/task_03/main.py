person = {"name": "Mariusz", "age": 30, "city": "Rzeszow"}

try:
    key = input("What information do you want? ")
    print(person[key])
except KeyError:
    print(f"Key: {key} dont exist in data")
