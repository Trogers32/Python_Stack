
from decimal import *
getcontext().prec = 3

class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, IDT):
        for i in range(len(self.products)-1):
            if self.products[i].ID == IDT:
                self.products[i].print_info()
                self.products.pop(i)
        del self
    def inflation(self, percent_increase):
        percent_increase = Decimal(percent_increase)
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
        return self