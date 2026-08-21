with open("shopping_list.txt", "a") as f:
    f.write("Milk\n")
with open("shopping_list.txt", "r") as f:
    data = f.read()
    print(data)
