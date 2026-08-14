## Polymorphism: it is the ability of a function or method to work in different ways depending on the object it is acting upon.
#  In Python, polymorphism can be achieved through method overriding and operator overloading.
#  

# WAP to show the use of polymorphism in python.

# class Animal:
#     def speak(self):
#         return "Animal sound"

# class Dog(Animal):
#     def speak(self):
#         return "barks"

# class Cat(Animal):
#     def speak(self):
#        return "meows"
    
# d=Dog()
# c=Cat()
# print(d.speak())
# print(c.speak())


# types of polymorphism in python:
# 1. Duck Typing: In Python, duck typing is a concept where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. If an object behaves like a certain type, it can be treated as that type, regardless of its actual class.
# 2. Operator Overloading: Operator overloading allows you to define how operators (like +, -, *, etc.) behave for objects of a class. You can implement special methods in your class to customize the behavior of operators when applied to instances of that class.
# 3. in python 
# 

# Show ing Duck Typing
from torch import Def

from torch import Def

class Bird:
    def fly(self):
        return "Bird is flying"
    
class Airplane:
    def fly(self):
        return "Airplane is flying"
    
def make_fly(entity):
    print(entity.fly())

# Demonstrating Duck Typing
bird = Bird()
airplane = Airplane()

make_fly(bird)
make_fly(airplane)






