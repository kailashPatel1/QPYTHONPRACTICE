
# def greet ():
#     print("Hello")

# greet()


# find  the reverse of the each element of the list

# def reverse_list(lst):
#     reversed_lst = []
#     for item in lst:
#         reversed_lst.append(item[::-1])
#     return reversed_lst
# print(reverse_list(['hello', 'world', 'python']))  



# WAP to check given year is leap year or not

# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(year, "is a leap year.")  
# else:
#     print(year, "is not a leap year.")



# WAP to print the sum of all even numbers from 1 to n

# n = int(input("Enter a number: "))
# sum=0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum += i

# print("Sum of even numbers from 1 to", n, "is:", sum)



# WAP to print the sum of all odd numbers from 1 to n

# sum=0
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 != 0:
#         sum += i
# print("Sum of odd numbers from 1 to", n, "is:", sum)



# WAP to lambda function to check whether given number is even or odd.

# is_even = lambda x: x % 2 == 0
# is_odd = lambda x: x % 2 != 0

# number = int(input("Enter a number: "))
# if is_even(number):
#     print(number, "is even.")
# else:
#     print(number, "is odd.")






# WAP to show the use of inheritance in python.

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def display(self):
#         super().display()
#         print("Age:", self.age)

# child = Child("Kailash", 20)
# child.display()





# WAP to show the use of polymorphism in python.

# class Animal:
#     def speak(self):
#         return "Animal sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Bird(Animal):
#     def speak(self):
#         return "Tweet!"

# Creating instances of each class
# dog = Dog()
# cat = Cat()
# bird = Bird()

# # Calling the speak method for each instance
# print(dog.speak())  
# print(cat.speak())  
# print(bird.speak())  



# WAP to print armstrong number between 1 to n
# n = int(input("Enter a number: "))
# for num in range(1, n + 1):
#     order = len(str(num))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     if num == sum:
#         print(num)






# Show run time polymorphism in python.
# class Car:
#     def __init__(self):
#         pass
# class Tire(Car):
#     def color(self):
#         return "Tire color is black"
        
# class Engine(Car):
#     def color(self):
#         return "Engine color is silver"

# T=Tire()
# E=Engine()

# print(E.color())

# print(T.color())





# Show the use of abstraction in python.
# import abc

# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# circle = Circle(5)
# print("Area of the circle:", circle.area())




# WAP to find the factorial of given number using recursion.

# def factorial(n):
#      # Base case: 0! and 1! are always 1
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input("Enter a number: "))
# print("Factorial of", n, "is:", factorial(n))



# 1.User-Defined Function

# def add(a, b):
#     return a + b
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# print("Sum:", add(n1, n2))


## 2. Lambda Function 

# multiply = lambda x, y: x * y
# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))
# print("Product:", multiply(n, m))
# print("Product:", multiply(5, 3))   # Example usage with fixed values

# # 3. Recursive Function 

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)         
#     if n <= 1:
#         return 1            
#     else:
#         return n * factorial(n - 1) 
        
# n=int(input("Enter a number: "))
# print("Factorial of", n, "is:", factorial(n))
    

# # 4. Generator Function
# def count_up_to(max_val):
#     count = 1
#     while count <= max_val:
#         yield count
#         count += 1
# n=int(input("Enter a number: "))
# for num in count_up_to(n):
#     print(num)

# WAP to find the sum of all even numbers from 1 to n using function.
# def sum_of_evens(n):
#     total = 0
#     for i in range(2, n + 1, 2):
#         total += i
#     return total

# n = int(input("Enter a number: "))
# print("Sum of even numbers from 1 to", n, "is:", sum_of_evens(n))

# WAP to find the sum of all odd numbers from 1 to n using function.


# def sum_odd(num):
#     sum=0
#     for i in range(1,num+1):
#         if i%2!=0:
#             sum+=i
#     return sum
# num=int(input("Enter a number:"))
# print("sum of Odd num from 1 to n",sum,"is",sum_odd(num))

# WAP to check num is palindrom or not
n=int(input("Enter a num:"))



