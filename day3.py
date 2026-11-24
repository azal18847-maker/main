
def hello1():
    hello2()
    print("hello1")
def hello2():
    hello3()
    print("hello2")
def hello3():
    hello4()
    print("hello3")
def hello4():
    print("hello4")


hello1()
