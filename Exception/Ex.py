# a=5
# b=0
# print(a/b)





# a = 20
# b = 0

# try:
#     result = a / b
#     print(result)
# except:
#     print("Something went wrong")




# a=5
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Num can not devide by Zero")



# age = input("Enter your age: ")

# try:
#     age = int(age)
#     print("Your age is:", age)

# except ValueError:
#     print("Please enter a valid number")



##Type Error

# a=25
# b="10"
# try:
#     age=a+b
#     print("your age is",age)
# except TypeError:
#     print("can not add int and string.")



## Index Error 

# num=[1,2,3,4]
# try:
#     print(num[5])
# except IndexError:
#     print("Enter invailid index.")



##KeyError 

# d={"name":"kailash","age":22}
# try:
#     print(d["marks"])
# except KeyError:
#     print("marks key not exist.")


## Mitiple Except 
#we can access multiple exception seperatly
# try:
#     a = int(input("Enter number 1: "))
#     b = int(input("Enter number 2: "))

#     result = a / b

#     print(result)

# except ValueError:
#     print("Please enter numbers only")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print(a//b)


#else : it exicute when no error ocure

# try:
#     a = 10
#     b = 2

#     result = a / b
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Division successful")
#     print(result)


# finally: it executes error ocure or not 

# try:
#     a = 10
#     b = 0
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program completed") 


## Complete Stracture of Exception handling

# try:
#     a = int(input("Enter number 1: "))
#     b = int(input("Enter number 2: "))

#     result = a / b
# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Execution completed")    


 


class User:
    def __init__(self,name):
        self.name=name
        self.leave="Apply"


class Admin:
    def leave(self,name):
        self.name=name
u=User("kailash")
u=Admin("AAa")       

