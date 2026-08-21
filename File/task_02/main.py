import json

car = {"brand": "fiat", "year": 2010, "car_mileage": 123123}

with open("car.json", "w") as f:
    json.dump(car, f, indent=4)


with open("car.json", "r") as f:
    data = json.load(f)
    print(data["brand"], data["car_mileage"], type(data))
