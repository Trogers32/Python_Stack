class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( name )
        return self
    def add_tiger(self, name):
        self.animals.append( name )
        return self
    def add_liger(self, name):
        self.animals.append( name )
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def display_info(self):
        print(f"{self.name} is {self.age} years old, their health level is {self.health}, and their happiness level is {self.happiness}")
    def feed(self):
        self.health += 10
        self.happiness += 10

class Tiger(Animal):
    def __init__(self, name, age=0, health=5, happiness=5, design="striped"):
        super().__init__(name, age, health, happiness)
        self.design = design
    def feed(self):
        super().feed()
        self.health += 2
        self.happiness += 2

class Lion(Animal):
    def __init__(self, name, age=0, health=10, happiness=10, design="bushy"):
        super().__init__(name, age, health, happiness)
        self.design = design
    def feed(self):
        super().feed()
        self.health += 5
        self.happiness += 6

class Liger(Animal):
    def __init__(self, name, age=0, health=20, happiness=2, design="bushy stripes"):
        super().__init__(name, age, health, happiness)
        self.design = design
    def feed(self):
        super().feed()
        self.health -= 4
        self.happiness += 20

zoo1 = Zoo("John's Zoo")
khan = Tiger("Khan")
rajah = Liger("Rajah")
simba = Lion("Simba")
nala = Lion("Nala")
zoo1.add_lion(nala).add_lion(simba).add_liger(rajah).add_tiger(khan).print_all_info()
khan.feed()
rajah.feed()
simba.feed()
zoo1.print_all_info()