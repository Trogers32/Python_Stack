from stores import Store
from products import Product

safeway = Store("Safeway")
wow = Product("Warcraft", 60, "Game",1)
sourdough = Product("Sourdough", 4, "Bread",2)
white = Product("White", 4, "Bread",3)
wheat = Product("Wheat", 4, "Bread",4)

def display():
    for i in safeway.products:
        i.print_info()
    print("___________________")

safeway.add_product(wow).add_product(sourdough).add_product(white).add_product(wheat)
display()

safeway.inflation(0.01)
display()

safeway.set_clearance("Bread", 0.01)
display()

safeway.sell_product(wow.ID)
print("\n\n\n")
display()


safeway.sell_product(sourdough.ID)
print("\n\n\n")
display()