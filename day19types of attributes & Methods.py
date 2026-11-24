"""
types of attributes and methods
there are 2 types of attribute one is a class attribute and another one is as object/instance attribute
there are 3 types of methods 
1) instance/object mothod - when your method is targeting object location that method is known as instance mehtod
2)class method - when your method is targeting class location that method is known as class method
3)static method - when you are not targeting any location you will use a static method
"""
class Factory:
    location = "Bhopal" #class attribute
    def __init__(self,ingredients):
        
        self.ingredients=ingredients          #instance/object attribute
    def details(self):
        print(self.ingredients)
    @classmethod
    def factory_info(cls): #class method
        print(f"""
              Factory is located in {cls.location}""")
    @staticmethod
    def hello():
        print("hello I am a static method")
obj = Factory("icecream")
obj.details()
obj.factory_info()