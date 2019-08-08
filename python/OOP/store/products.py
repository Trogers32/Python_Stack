from decimal import *
getcontext().prec = 3
class Product:
    def __init__(self, name, price, category, ID):
        self.name = name
        self.price = Decimal(price)
        self.category = category
        self.ID = ID
    def update_price(self, percent_change, is_increased):
        percent_change = Decimal(percent_change)
        if is_increased == True:
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
        return self
    def print_info(self):
        print("___________________")
        print(f"| {self.name} {self.category} |\n| Price: ${self.price} |")
        return self
