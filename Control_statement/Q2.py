# write a program to print value as it is only if the lenth of value is even.

# Q2  

# user='saurabh_khare'
# passw=12334


# name=input("Enter your name:")
# password=input("Enter your password:")
# if name==user:
#     password=input("Enter the password")
#     if password==passw:
#         print("Login")
#     else:
#         print("you are entering wrong password.")
# else:
#     print("invailid user.")


# Q3. wap to print middle value of a list only if it is string
# l=eval(input("Enter the list"))

# l=[True,"hello","bye",8,3.6]
# if type(l)==list:
#     if  len(l)%2 !=0:
#         middle=l[len(l)//2]
#         if type(middle)==str:
#           print('Middle')
#     else:
#         print("Does not cotain middle value.")
# else:
#     print("Input is not list.")



# Q4.Wap to check given char is vowel or consonant.


# Q5 WAP to find gretest of 4 num without using and elif

# a=2
# b=3
# c=4
# d=5

# if a>b:
#     if a>c:
#         if a>d:
#          print("A is greater")
#         else:
#            print(d,"is greater")
#     else:
#        if c>d:
#           print(c,"is greater")

#        else:
#           print(d,"is greater")
# else:
   

#   WAP to find 2nd greatest num in 4 value.
# a=3
# b=4
# c=5
# d=6

# if a>b and a>c and a>d:
#     if a>c:
#         if b>d:





# WAP to toggle a string.

# s="Hello World"
# out=''
# i=0
# while i<len(s):
#     if "a"<= s[i]<="z":
#         out +=chr(ord(s[i])-32)
#     elif "A"<= s[i]<="Z":
#          out +=chr(ord(s[i])+32)
#     else:
#         out+=s[i]
#         i+=1
# print(out)

    
# WAP to reverse the given number

# n=123
# rev=0
# while n!=0:
#     id=n%10
#     rev = rev*10+id
#     n=n//10
# print(rev)


#WAP to check num is perfect or not.

# n=int(input("Enter a num:"))
# totle=0
# i=1
# while n>i:
#     if n%i==0:
#         totle=totle+i
#     i=i+1
# if totle==n:
#     print(n," Is perfect num:")
# else:
#     print(n," is Not perfect")




    
# WAP to extract all the even integers present in tuple at odd index.

# t=(True,33,2.3,25,54,22,56,3+2j)
# out=[]
# i=0
# while i < len(t):
#     if i%2!=0 and type (t[i])==int and t[i]%2==0:
#         out.append(t[i])
#     i=i+1
# print(out)




# WAP to remove duplicate from list without using set

# l=[2,3,4,2,4,3,1]
# res=[]
# i=0
# while i < len(l):
#     if l[i] not in res:
#         res.append(l[i])
#     i=i+1
# print(res)




# WAP to sum off all the odd num between given range.

# n1=int(input("Enter 1st num:"))
# n2=int(input("Enter 2nd num:"))
# n2=0
# gr=0
# small=0
# if n1>n2:
#     small=n2
#     gr=n1
# else:
#     small=n1
#     gr=n2
# total=0
# i=small
# while i < gr:
#     if i%2 !=0:
#         total=total+i
#     i=i+1
# print(total)    




# WAP to find max num in list.

# l=[2,3,5,7,9,8,1,0]
# gr=l[0]
# i=0
# while i<len(l):
#     if l[i]>gr:
#         gr=l[i]
#     i=i+1
# print(gr)




# WAP to find the sum of cube of a num in string.
# num = input("Enter a number: ")   # Input as string

# sum_cube = 0

# for digit in num:
#     sum_cube += int(digit) ** 3

# print("Sum of cubes =", sum_cube)




# WAP to find sum of cube of a number in a string.

# email="kailash102004@gmail.com"

# total=0
# i=0
# while i< len(email):
#     if '0'<= email[i]<='9':
#         total=total+ int (email[i])**3
#     i=i+1
# print(total)



# WAP to check given num is Armstrong or not.

# n=153
# num=n
# total=0
# power=len(str(n))

# while n!=0:
#     ld=n%10
#     total=total+ld**3
#     n=n//10
#     if total==num:
#         print("Armstrong")
# else:
#     print("Not Armstrong.")











# WAP to check num is prime or not.

# n=int(input("Enter a number:"))
# for i in range(2,n):
#     if(n%i)==0:                        
#         print("Number is not prime")  
#         break  
# else:
#  print("Number is prime")





# break : it is a key word to terminate loop by passing some conditions
# Example

# i=1
# while i<=10:
#    if i==7:
#       break
# print(i)
# i=i+1



# continue : it is a key word use to skip current iteration.

#/i=1
# while i<=10:
#    if i==5:
#       continue
# print(i)
# i=i+1


# pass : it is placeholder of program


