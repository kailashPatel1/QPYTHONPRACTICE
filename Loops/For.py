## For Loop:  it is self iterative loop 
# note: initilizatin and updation is not mendetory in for loop
# we can use for loop on every collection data types exam: string, list, tuple, set,Dictionary, range

# Syntax:   for var in collection
                # code to execution 

# OR 

# For loop is a looping stataement in which variable pics one value at time from collections and for that specific value 
# it goinging to execute the entire block of code.
#  How many num of values present inside the collections that many num of time for is going executed.
 



#1.Range fun: it will generates the sequence of integers w/b geven specified limit
#   Syntax:  range(SV,EV,UP)

# a=list(range(1,11,1))
# print(a)

# b=tuple(range(0,20,2))
# print(b)
# c=set(range(2,10))
# print(c)




# 71.print all num present in list 
# l=[2,3,4,5,6,4+3j,True,'hii']
# for i in l:
    #   if type(i)==int 
#     print(i)




#72. WAP to extract all even num present in list

# l=[1,2,3,4,5,6,7,8,9,'hi',9.0]
# out=[]
# for i in l:
#      if type(i)==int and i%2==0:
#         out.append(i)
# print(i)



# 73. WAP to remove duplicate from list 


# l=[2,3,2,4,1,2,6,4,7,7,"hi","hi"]

# unic=[]
# for i in l:
#     if i not in unic:
#       unic.append(i)
# print(unic)



# 74.WAP to reverse string without using slicing

# s="Kailash"
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)





# WAP to Extract all lower case from string only if the ascii value is even

# s="Kailash_Patel" 
# out=""
# for i in s:
#     # if s.islower():
#     if 'a'<=i<='z'and ord(i)%2==0:
#         out=out+i
# print(out)


        

# WAP to lenth of homogenous tuple without len.


# t=(5,5,20,23,43,"hii",21)
# count=0
# homo=type(t[0])
# for i in t:
#     if type(i)!=homo:
#         print("Tuple is hetro")
#         break
#     else:
#         count=count+1
# else:
#     print("the lenth of tuple is:",count)




# 78.WAP to extract all key value pair from dictinory if key are string datatype and keys are integer 

# d={"a":1,"b":2,"c":3,"d":4}
# out={}
# for i in d:
#     if type(i)==str and type(d[i])==int:
#         out[i]=d[i]
# print(out)




#82. WAP to Extract all the non defaut values from list.

# l=[True,(),8.3,0j,False,'hello',45]
# out=[]
# for i in l:
#     if bool(i)==True:
#         out.append(i)
# print(out)



#83. WAP to check list is Homogenous or not 

# l=[2,3,4,5,6,7,8,'hi']
# homo=type(l[0])
# for i in l:
#     if type(i)!=homo:
#         print("Hetroge")
#         break
# else:
#     print("Homoge")

 
#84.WAP to replace the space by * present in string 

# s="hi i'm Kailash Patel"
# # a=s.replace(' ','*')
# # print(a)
# out=' '
# for i in s:
#     if i==' ':
#         out+='*'
#     else:
#         out+=i
# print(out)


#85 WAP to count the num of occurrence of a specified character.

# s=input("Enter the string:")
# char=input("Enter the character:")
# count=0
# for i in s:
#     if i==char:
#         count+=1
# print(f'The occurance of "{char}" is {count} times')


# 86 WAP to get following output.
# s='always keep smiling'
# out='syawla peek gnilims'

# s='always keep smiling'.split()
# out=''
# for i in s:
#     out+=i[::-1]+' '
# print(out)



# 87.WAP to get following output





# WAP ti get following  output.

# S=["jiooinema.com","file.Py","web.html","amazon.com","www.org"]
# out=["com","Py","html","org"]

# S=["jiooinema.com","file.Py","web.html","amazon.com","www.org"]
# out=[]
# for i in S:
#     ex = i.split('.')[-1]
#     if ex not in out:
#         out.append(ex)
# print(out)



# WAP to get following output
# s=["jiocinema.com","file.py","web.html","amazon.com","www.org"]
# out={'com': ['jiocinema'], 'py': ['file'], 'html': ['web'], 'org': ['www', 'www']}

# s=["jiocinema.com","file.py","web.html","amazon.com","www.org"]
# out={}
# for i in s:
#     ft,ex=i.split(".")
#     if  ex not in out:
#        out[ex]=[ft]
# else:
#     out[ex]+=[ft]
#     print(out)



# Extract all the even integers between 1 to n.
# n=int(input("Enter a num:"))
# out=[]
# for i in range(1,n+1):
#     if i%2==0:
#         out.append(i)
# print(out)



# Extract all the odd num b/w 1 to n
# n=int(input("Enter a num:"))
# out=[]
# for i in range(1,n+1):
#     if i%2!=0:
#         out.append(i)
# print(out)




# Extract the character present at odd index

# s="KailshPatel"
# ch=''
# for i in range(len(s)):
#     if i%2 !=0:
#         ch=ch+s[i]
# print(ch)




# WAP to print left angle triangle pattern using for loop

# n=eval(input("Enter a num:"))
# for i in range(1,n+1):
#     print("*"*i)



# WAP to print left inverse angle triangle pattern using for loop
# n=eval(input("Enter a num:"))
# for i in range(1,n+1):
#     print("*"*(n-i+1))



# WAP to print right angle triangle pattern using for loop
# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)




# WAP to print right inverse angle triangle pattern using for loop
# n=int(input("Enter a num:"))
# for i in range(1,n+1):      
#     print(" "*i+"*"*(n-i+1))



# daimond pattern using for loop
# n=int(input("Enter a num:"))
# for i in range(1,n+1):  
#     print(" "*(n-i)+"*"*(2*i-1))



# WAP to extract all the string values present in list only if the string is palindrome

# l=[True, 'mom',3.5,'dad','aya']
# out=[]
# for i in l:
#     if type(i) ==str and i == i[::-1]:
#         out.append(i)
# print(out)




# Prime num without break

# n=int(input("Enter a number:"))
# c=0
# for i in range(2,n):
   




# prime num with break 

# n=int(input("Enter a number:"))
# for i in range(2,n):
#     if(n%i)==0:                        
#         print("Number is not prime")  
#         break  
# else:
#  print("Number is prime")





# ############ NESTED FOR LOOP ##########

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)



# WAP to get the following output. without length function.

# s="Kailash patel".split()
# out={}
# for i in s:
#     count=0
#     for j in i:
#         count+=1
#         out[i]=count
# print(out)



# WAP to get following output
# s='power star'
# out={'power':2,'star':1}  (num of vowel is key).


# s="power star".split()
# out={}
# for i in s:
#     count=0
#     for j in i:
#         if j in "aeiouAEIOU":
#              count+=1
#         out[i]=count
# print(out)









# WAP  to get following output
# s="kabab is love"
# out={'kb':('kbb',3,'bbk'),'is':('s','l','s'),'le':('lv','2','vl')}
# {list + list char:   (consonant,no of consonant,rev of consonant)}


# s="kabab is love"
# out={}
# for i in s:
#     cons=''
#     for j in i:
#         if j not in 'AEIOUaeiou':
#             cons +=j
#             out[i[0]+i[-1]] = (cons,len(cons),cons[::-1])
# print(out)




# WAP  to get the following output.
# In='bacbcaabbaa'
# out=b4a5c2

# In='bacbcaabbaa'
# out=''
# for i in In:
#     count=0
#     for j in i:
#         if i==j:
#             count +=1
# print(out)



##############

# In=[10,20,18]
# out=[]
# for i in In:
#         out.append(sum(In)-i)
# print(out)






# WAP to take a string as input and disply each and every character of string line by line.

# s="Kailash"
# for i in s:  
#     print(i)


# WAP take list as input and squre aech element present in list 

# l=eval(input("enter your list"))
# for i in l:
#     print(i**2) 



# WAP add all item that prenst inside a tuple 

# t=eval(input("enter your tuple:"))
# sum=0
# for i in t:
#     sum=sum + i
# print(sum)




###############################
# In=[100,200,35,40,60]
# out=[]
# for i in In:
#     to=0
#     for j in In:
#         if i !=j:
#             to +=j
#     out.append(to)
# print(out)



# count function:- it will return the count of element occurred in collection.
# Syntax:
    # var.count(element)


# name='kailash_Patel'
# n=name.count('a')
# print(n)




# WAP to get following output
# I=[100,200,50,400,300]
# N=300
# out=[[100,200],[300]]

# I=[100,200,50,400,300]
# N=300
# out=[]

# for i in I:
#     if i==N:
#         out.append([i])
#     else:
#         for j  in I:
#             if i + j == N:
#                 if [i,j] not in out:
#                     out.append([i,j])
#                 out.extend([i,j])
# print(out)


# print prime num





# WAP to check given num is strong or not.# n=145 

# n = int(input("Enter a number: "))
# temp = n
# sum_fact = 0

# while temp > 0:
#     digit = temp % 10

#     # Find factorial of the digit
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i

#     sum_fact += fact
#     temp //= 10
# # Check Strong Number
# if sum_fact == n:
#     print(n, "is a Strong Number")
# else:
#     print(n, "is not a Strong Number")






# WAP to check given num is perfect or not. # n=6  1+2+3=6

# n = int(input("Enter a number: "))
# sum_divisors = 0

# for i in range(1, n):
#     if n % i == 0:
#         sum_divisors += i

# if sum_divisors == n:
#     print(n, "is a Perfect Number")
# else:
#     print(n, "is not a Perfect Number")


 

####### Pattern #########

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()



####################



# Print Star in daigonal

# for i in range(1,6):
#     for j in range(1,6):
#         if i ==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# #######

# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



#####################

# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1 or i ==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()





# ##########

# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==n//2+1 or j ==n//2+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()




############*############

# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==n//2+1 or j ==n//2+1 or i+j==n+1 or i ==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()





#######################


# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i ==n or j==1 or j ==n  or i==n//2+1 or j ==n//2+1 or i+j==n+1 or i ==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# #### right tringle #####
# n=eval(input("Enter a num:"))
# for i in range(1,n+1):
#     print("*"*i)




# daimond pattern using for loop

# n=int(input("Enter a num:"))
# for i in range(1,n+1):  
#     print(" "*(n-i)+"*"*(2*i-1))


###########


# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==n//2+1 or j ==n//2+1 or i+j==n+1 or i ==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()







# WAP to take a string as input and display each char of a string 

# s="Kailash"
# for i in s:
#     print(i)



# WAP to count how many num of vowel do we have in string 

# s="Kailash_Patel"
# count=0
# for i in s:
#     if i in "aeiou":
#         count=count+1
# print(count)


# WAP to count how many num of consonent do we have in string.

# WAP to take list as input and add all item prent inside in list

# l=eval(input("enter your list:"))
# sum=0
# for i in l:
#     sum=sum+i
# print("Sum of all element present in list:",sum)



# WAP to take list as input and  multiply all item prent inside in list

# l=eval(input("enter your list:"))
# mul=1
# for i in l:
#     mul=mul*i
# print("Sum of all element present in list:",mul)


# WAP to add all even num present inside list.
# WAP to all those element which are present inside a list, which is divisible by both 3 and 5



# WAP to print the factorial of a given num.

# n=int(input("Enter a num:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial is:",fact)




### WAP to print the fibonacci series up to a given lenght.###imp

# length=int(input("Enter the length:"))
# n1=0
# n2=1
# print(n1,n2,end=" ")
# for i in range(length - 2):
#     next = n1 +n2
#     print(next,end=" ")
#     n1=n2
#     n2=next




# WAP calculate lcm of two num

# n1=int(input("Enter 1st num:"))
# n2=int(input("Enter 1st num:"))

# if n1>n2:
#     small=n1
# else:
#     small=n2
#     for i in range(1,small+1):
#         if n1%i==0  and n2%i==0:
#             hcf=i
#     lcm=(n1*n2) /hcf
# print("LCM of gien num:",lcm)       



# coprime: num are sed to be coprime to each other if there hcf is equal to 1.
# WAP to check a given num are coprime are not 


# n1=int(input("Enter 1st num:"))
# n2=int(input("Enter 1st num:"))
# if n1>n2:
#     small=n1
# else:
#     small=n2
# for i in range(1,small+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
#         if hcf==1:
#             print("num are coprime to each other.")
#         else:
#             print("num are not coprime to each other.")





# WAP to check given num is perfect num or not 

# num=int(input("Enter your num:"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print(num,"is perfect num.")   
# else:
#     print(num,"is not perfect num.")     
        


# WAP to dupliactes element from list

# l=[2,'hi',3,2,3,4,5,'hi','ram']
# out=[]

# for i in l:
#     if i  not in out:
#         out.append(i)
        
# print(out,sum)



# WAP to add unic element inside the given list: 

# l=[2,3,2,3,4,5]
# out=[]
# sum=0
# for i in l:
#     if i  not in out:
#         out.append(i)
#         sum=sum+i
# print(sum)


# WAP to add all the repeated element only 


l=eval(input("enter your list:"))
res=[]

for i in l:
    if i not in res:
        res.append(i)      
sum=0
for i in res:
        if l.count(i)>1:      
            sum=sum+(i*l.count(i))
print("sum of all repeated num is:",sum)



# WAP To add those num which are not reapeted in list


