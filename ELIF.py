# elif : when we have multiple condition to veryfy we use elif statement.
#        if a condition is true then tast will get exicuted and rest of the condition will get rejected automatic, if nun of condition is true then else executed.
# 

# WAP to check relation b/w two integer num:

# n1=int(input("enter a num"))
# n2=int(input("enter a num"))
 
# if n1>n2:
#     print("n1 is greater num.")
# elif n2>n1:
#     print("n2 is greater num.")   
# else:
#     print("n1 and n2 is equal.") 
                    


# 20.WAP to check given integer is single digit or two digit or three digits or more than three digit.
# n=int(input("enter a num:"))
# if 0<=n<=9:
#     print("single")
# elif 10<=n<=99:
#     print("double")
# elif(100<= n<=999):
#     print("triple")
# else:
#     print("more than three.")



# 21. check char is uppercase, lowercase, digit, or special char

# char = input("enter a char: ")
# if char.isupper():
#     print("uppercase")
# elif char.islower():
#     print("lowercase")
# elif char.isdigit():
#     print("digit")
# else:
#     print("special character")



 #WAP to find given number is prime or not 

# n=int(input("Enter a number:"))
# for i in range(2,n):
#     if(n%i)==0:                        
#         print("Number is not prime")  
#         break  
# else:
#  print("Number is prime")



# WAP to print factoreal num using for loop   

# num=int(input("Enter a num:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("Factoreal is:",fact)




# Remove duplicate elements from a list while preserving order.

# lst=[2,3,2,5,4,5,2]

# result=[]
# for i in lst:
#     if i not in result:
#         result.append(i)
# print(f"After removing duplicates:{result}")







# WAP to check given num is positive, negative or Zero


# n=int(input("Enter a num:"))

# if 0<n:
#     print(n,"num is positive")
# elif n==0:
#     print(n,"num is zero.")
# else:
#     print(n,"num is negative.")




# WAP to find lagest among three num.

# n1=int(input("Enter a num:"))
# n2=int(input("Enter a num:"))
# n3=int(input("Enter a num:"))

# if n1>n2 and n1>n3:
#     print(n1," n1 is greater")
# elif n2>n3:

#     print(n2,"n2 is greater num")
# elif n1==n2 and n2==n3:
#     print("All num is Equal ")
# else:
#     print(n3,"n3 is greater num.")




# WAP to  check given leap year or not
