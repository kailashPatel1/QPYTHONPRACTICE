## Polymorphism: it is the ability of a function or method to work in different ways depending on the object it is acting upon.
#  In Python, polymorphism can be achieved through method overriding and operator overloading.
#  

# WAP to show the use of polymorphism in python.

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"
    