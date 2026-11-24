# class Animal:
#     a=12
#     def __init__(self,name):
#         self.name=name
#     def hello(self):
#         print("hello")
# class human:
#     b=23
#     def __init__(self,age):
#         self.age=age
#     def hello(self):
#         print("I am a human world best human")
# class robot(Animal,human):
#     def __init__(self,name,age):
#         Animal.__init__(self,name)
#         human.__init__(self,age)
# obj = robot("Chitti",1)
# print(obj.name)
# print(obj.age)
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        return f"your details are {self.name} , {self.age}"
class Human(Animal):
    def __init__(self,name,age,number):
        super().__init__(name,age)
        self.number=number
    def details(self):
        print(super().details())
        print(self.number)
obj= Human("Haarsh",24,7775432178)
obj.details()
#method overriding happens when you are applying inheritance and in both parent and child class you have same method name so child class method overrides the parent class method and the object of child class cannot the parent class method








