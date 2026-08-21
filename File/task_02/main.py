import json

cars = [
    {"brand": "fiat", "year": 2010},
    {"brand": "bmw", "year": 2018},
    {"brand": "audi", "year": 2021},
]

with open("garage.json", "w") as f:
    json.dump(cars, f, indent=4)


with open("garage.json", "r") as f:
    garage_data = json.load(f)
    for car in garage_data:
        print(car["brand"])
