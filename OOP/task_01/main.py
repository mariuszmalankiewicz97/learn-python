class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"Produkt: {self.name}\nCena: {self.price} zł\nIlość: {self.amount}"


class Warehouse:
    def __init__(self):
        self.stock = {}

    def set_product(self, product):
        self.stock[product.name] = product

    def add_product(self, product, amount):
        if product.name in self.stock:
            self.stock[product.name].amount = self.stock[product.name].amount + amount
            return True
        return False

    def show_stock(self):
        for item in self.stock.values():
            print(f"{item}\n")

    def spend_product(self, product, amount):
        if product.name in self.stock and amount <= self.stock[product.name].amount:
            self.stock[product.name].amount = self.stock[product.name].amount - amount
            return True
        return False

    def value_product(self, product):
        price = self.stock[product.name].price
        amount = self.stock[product.name].amount
        return price * amount


magazyn = Warehouse()

laptop = Product("Laptop", 3000, 5)
telefon = Product("Telefon", 1000, 10)
mysz = Product("Mysz", 200, 50)
magazyn.set_product(laptop)
magazyn.set_product(telefon)
magazyn.set_product(mysz)
magazyn.spend_product(laptop, 2)
magazyn.value_product(laptop)
print(magazyn.stock["Laptop"].amount)
magazyn.add_product(laptop, 10)
print(magazyn.stock["Laptop"].amount)
magazyn.show_stock()
