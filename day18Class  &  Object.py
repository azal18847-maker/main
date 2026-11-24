class Factory:
    name ="Puma"
    def details(self):
        print("hello this is puma factory")
        
a = Factory()
#objects can also access attributes and methods defined inside the class
print(a.name)
a.details()
#when you call any method using an object your object location is passed
#a constructor function is a type of dunder method that will be automatically called once upon you to create your object and it will also capture the location of your object
class Regestration :
    def __init__(self):
        print(self)
        print("hello how are you")
        
    print("hello")


a= Regestration()
b= Regestration()
c= Regestration()
"""
types of attributes and methods
there are 2 types of attribute one is a class attribute and another one is as object/instance attribute
"""
class Factory:
    location = "Bhopal" #class attribute
    def __init__(self,ingredients):
        self.ingredients=ingredients#instance/object attribute

