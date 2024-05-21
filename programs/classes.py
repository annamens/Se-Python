class Ran:

    name="ramesh"
    def __init__(self,x,y): #self refers to its own instance and can be accessed within class or with class instance
        self.x=x
        self.y=y
    @classmethod #class object can be instantiated with the instance or class name, it has access to class attr
    def me(cls,name):
        print("me ", name)

    @staticmethod #static methods are independent of class, they
    # have own parameters, they are like functin but kept inside a class
    def stat(name,age):
        return name,age

r =Ran(1,2)
r.me("book")
print(r.name)
Ran.me("srini")
print(Ran.stat('srini',28))


class Parent:
    def __init__(self):
        self.__age= 10

    @property
    def get_age1(self):
        self.__age = 31
        return self.__age

    def get_age(self):
        return self.__age
class Child(Parent):
    def print_pvt(self):
        print("printed pvt var: ",self.get_age())

    def print_prop_age(self):
        print(self.get_age1)

child=Child()
child.print_pvt()
child.print_prop_age()