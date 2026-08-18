##Example of map with lamda 

# num=[1,2,3,4,5,6,7,8]
# squ=map(lambda x: x**2,num)
# print("Squre of num is:",list(squ))

######

# numbers=[1,2,3,4,5,6]

# even=map(lambda x: x**2,numbers)

# print(list(even))


########

numbers = [1, 3, 4, 6]

evens = filter(lambda x: x % 2 == 0, numbers)     

print(list(evens))


