# function: it is name given to memory block, where the set of instractions are
#  stored and perfoming some specific task.

# why we need  Functions:
# 1.> we can reduce the num of instractions
# 2.> we can increase the efficency of the code.
# 3.> we cav avoid code repitition.
# 4.> reuse code for n num of time.



### types:
# 1. Inbuilt function: it is the function which are already defined in python and we can use them directly in our code.
# 2. User-Defined Functions: it is the function which are defined by user to perform some specific task. we can call them when ever we want to use them in our code.



1
## Inbuilt function: it is the function which are already defined in python and we can use them directly in our code.
#              



### Inbuilt Function Types:

# a) Utility Functions

# The inbuilt functions that we can use with different data types.

# b) Functions of List

# The functions/methods that we can use with list.

# c) Functions of String

# The functions/methods that we can use with string.

# d) Functions of Tuple

# The functions/methods that we can use with tuple.

# e) Functions of Set

# The functions/methods that we can use with set.

# f) Functions of Dictionary

# The functions/methods that we can use with dictionary.

## A. Utility Functions
# 1. type()

# It will return the data type of a variable/value.

# Syntax:

# type(variable)

# Example:

# a = 10
# print(type(a))


# 2. id()
        # It will return the unique identity/address reference of an object.

# Syntax:

# id(variable)

# Example:

# a = 10
# print(id(a))

# 3. bool()

    #   It will convert a value into Boolean value, i.e. True or False.

# Syntax:

# bool(value)

# Example:

# a = 10
# print(bool(a))


# 4. eval()

# It will evaluate a string as a Python expression.

# Syntax:

# eval(expression)

# Example:

# a = "10 + 20"
# print(eval(a))


# B. String Functions

#        These are functions/methods which are mainly used with strings.

# 1. len()

    #  It will return the length of a collection/string.

# Syntax:

# len(variable)

# Example:

# name = "Kailash"
# print(len(name))



# 2. split()

        #  It will split a string into parts and store the result in a list.

# Syntax:

# var.split()
# 
# Example:

# name = "Kailash Patel"
# print(name.split())


# 3. input()

# It is used to accept a value from the user.

# Syntax:

# input()

# Example:

# name = input("Enter your name: ")
# print(name)

# 4. replace()

# It will replace old characters/string with new characters/string.

# Syntax:

# var.replace('old_char', 'new_char')

# Example:

# name = "Kailash"
# print(name.replace("K", "M"))


# 5. upper()

# It will convert all characters into uppercase.

# Syntax:

# var.upper()

# Example:

# name = "kailash"
# print(name.upper())


# 6. lower()

# It will convert all characters into lowercase.

# Syntax:

# var.lower()

# Example:

# name = "KAILASH"
# print(name.lower())


# 7. islower()

# It will check whether all alphabetic characters are lowercase.

# Syntax:

# var.islower()

# Example:

# name = "kailash"
# print(name.islower())


# 8. isupper()

# It will check whether all alphabetic characters are uppercase.

# Syntax:

# var.isupper()

# Example:

# name = "KAILASH"
# print(name.isupper())


# 9. isalpha()

# It will return True if all characters are alphabets.

# Syntax:

# var.isalpha()

# Example:

# name = "Kailash"
# print(name.isalpha())


# Note: Space and numbers are not considered alphabets.

# name = "Kailash Patel"
# print(name.isalpha())

# 10. ord()

# It will return the ASCII/Unicode value of a character.

# Syntax:

# ord('char')

# Example:

# print(ord('A'))


# 11. chr()

# It will return the character for a particular Unicode/ASCII value.

# Syntax:

# chr(value)

# Example:

# print(chr(65))


# 12. title()

# It will convert the first character of every word into uppercase.

# Syntax:

# var.title()

# Example:

# name = "kailash patel"
# print(name.title())



# 13. capitalize()

# It will convert the first character of the string into uppercase.

# Syntax:

# var.capitalize()

# Example:

# name = "kailash patel"
# print(name.capitalize())


# 14. count()

# It will count the occurrence of a particular character/string.

# Syntax:

# var.count('character')

# Example:

# name = "banana"
# print(name.count("a"))


# 15. swapcase()

# It will convert uppercase characters into lowercase and lowercase characters into uppercase.

# Syntax:

# var.swapcase()

# Example:

# name = "Kailash PATEL"
# print(name.swapcase())


# C. Functions of List

# These methods are used with list.

# 1. append()

# It will add one element at the end of the list.

# Syntax:

# list.append(element)

# Example:

# a = [10, 20, 30]
# a.append(40)
# print(a)


# 2. pop()

# It will remove and return an element from the list. By default, it removes the last element.

# Syntax:

# list.pop()

# Example:

# a = [10, 20, 30]
# a.pop()
# print(a)


# 3. extend()

# It will add multiple elements from another collection to the list.

# Syntax:

# list.extend(collection)

# Example:

# a = [10, 20]
# a.extend([30, 40])
# print(a)


# 4. remove()

# It will remove the first occurrence of a particular element.

# Syntax:

# list.remove(element)

# Example:

# a = [10, 20, 30]
# a.remove(20)
# print(a)


# 5. insert()

# It will insert an element at a particular index.

# Syntax:

# list.insert(index, element)

# Example:

# a = [10, 30]
# a.insert(1, 20)
# print(a)


# 6. sort()

# It will arrange the elements of the list in ascending order.

# Syntax:

# list.sort()

# Example:

# a = [30, 10, 20]
# a.sort()
# print(a)


# 7. reverse()

# It will reverse the order of elements in the list.

# Syntax:

# list.reverse()

# Example:

# a = [10, 20, 30]
# a.reverse()
# print(a)




# 8. count()

# It will count how many times an element occurs in the list.

# Syntax:

# list.count(element)

# Example:

# a = [10, 20, 10, 30, 10]
# print(a.count(10))


# 9. clear()

# It will remove all elements from the list.

# Syntax:

# list.clear()

# Example:

# a = [10, 20, 30]
# a.clear()
# print(a)


# D. Functions of Tuple

# Tuple is immutable, so it has fewer methods.

# 1. count()

# It will count the occurrence of an element in the tuple.

# Syntax:

# tuple.count(element)

# Example:

# a = (10, 20, 10, 30)
# print(a.count(10))


# 2. index()

# It will return the index/position of the first occurrence of an element.

# Syntax:

# tuple.index(element)

# Example:

# a = (10, 20, 30)
# print(a.index(20))


# E. Functions of Set
# 1. add()

# It will add one element to the set.

# Syntax:

# set.add(element)

# Example:

# a = {10, 20}
# a.add(30)
# print(a)
# 2. remove()

# It will remove a specified element from the set. If the element does not exist, it gives an error.

# Syntax:

# set.remove(element)

# Example:

# a = {10, 20, 30}
# a.remove(20)
# print(a)

# 3. discard()

# It will remove a specified element from the set. If the element does not exist, it does not give an error.

# Syntax:

# set.discard(element)

# Example:

# a = {10, 20, 30}
# a.discard(50)
# print(a)
# 4. pop()

# It will remove and return an arbitrary element from the set.

# Syntax:

# set.pop()

# Example:

# a = {10, 20, 30}
# a.pop()
# print(a)
# 5. clear()

# It will remove all elements from the set.

# Syntax:

# set.clear()

# Example:

# a = {10, 20, 30}
# a.clear()
# print(a)


# 6. union()

# It will return all unique elements from two or more sets.

# Syntax:

# set1.union(set2)

# Example:

# a = {10, 20, 30}
# b = {30, 40, 50}

# print(a.union(b))


# 7. intersection()

# It will return common elements between two sets.

# Syntax:

# set1.intersection(set2)

# Example:

# a = {10, 20, 30}
# b = {20, 30, 40}

# print(a.intersection(b))


# 8. difference()

# It will return elements that are present in the first set but not in the second set.

# Syntax:

# set1.difference(set2)

# Example:

# a = {10, 20, 30}
# b = {20, 30, 40}

# print(a.difference(b))


# F. Functions of Dictionary
# 1. keys()

# It will return all keys of the dictionary.

# Syntax:

# dict.keys()

# Example:

# a = {"name": "Kailash", "age": 22}
# print(a.keys())

# 2. values()

# It will return all values of the dictionary.

# Syntax:

# dict.values()

# Example:

# a = {"name": "Kailash", "age": 22}
# print(a.values())
# 3. items()

# It will return all key-value pairs.

# Syntax:

# dict.items()

# Example:

# a = {"name": "Kailash", "age": 22}
# print(a.items())
# 4. get()

# It will return the value of a specified key.

# Syntax:

# dict.get(key)

# Example:

# a = {"name": "Kailash", "age": 22}
# print(a.get("name"))


# 5. update()

# It will add or update key-value pairs in the dictionary.

# Syntax:

# dict.update({key:value})

# Example:

# a = {"name": "Kailash"}
# a.update({"age": 22})
# print(a)


# 6. pop()

# It will remove a specified key-value pair from the dictionary.

# Syntax:

# dict.pop(key)

# Example:

# a = {"name": "Kailash", "age": 22}
# a.pop("age")
# print(a)


# 7. popitem()

# It will remove and return the last inserted key-value pair.

# Syntax:

# dict.popitem()

# Example:

# a = {"name": "Kailash", "age": 22}
# a.popitem()
# print(a)


# 8.clear()

# It will remove all key-value pairs from the dictionary.

# Syntax:

# dict.clear()

# Example:

# a = {"name": "Kailash", "age": 22}
# a.clear()
# print(a)


# 9. copy()

# It will create a copy of the dictionary.

# Syntax:

# dict.copy()

# Example:

# a = {"name": "Kailash"}
# b = a.copy()

# print(b)




# 2.User Defined Function

# User Defined Function:
# These are the functions which are created/defined by the programmer according to their requirement.

# We use the def keyword to create a user-defined function.

# Syntax:
#     def function_name():
#     statement
# Example:


# WAP to traverse a list and print each element of the list.
# def print_list_elements(lst):
#     for element in lst:
#         print(element)

# my_list = [1, 2, 3, 4, 5]
# print_list_elements(my_list)



# l=[1,2,3,4,4,5,6,7,8,9,10]
# res=[]
# for i in l:
#     if i%2==0:
#         res.append(i)
# print(res)
     




# Example of args and kwargs 


