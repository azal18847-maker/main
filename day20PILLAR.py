"""
pillars
inheritance 
inheritance works between classes

"""
class Factory:
    def __init__(self,milk,sugar):
        self.milk = milk
        self.sugar=sugar
    def quantity(self):
        print(f"Total quantity will be {(self.milk + self.sugar)//1.5}")
class Factory_two(Factory):
    def __init__(self,milk,sugar,flavour):
        super().__init__(milk,sugar)
        self.flavour = flavour    
    def quantity(self):
        super().quantity()
        print(f"your flavour is {self.flavour}")
yash = Factory_two(20,7,"vanilla")
azal = Factory(10,3)

azal.quantity()
yash.quantity()


#multilavel inheritance
class animal:
    def __init__(self,species):
        self.species = species
    def details(self):
        print(f"you are a animal and your species is {self.species}")
class human(animal):
    pass
class robot(human):
    pass
onj = robot("human")
onj.details()