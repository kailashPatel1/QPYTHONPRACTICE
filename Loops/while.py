#39. Wap to print natural number
# n=int(input("Enter a num:"))
# i=1
# while i<=n:
#     print(i)
#     i=i+1



# 40. Wap to print multiplication table for n.

# n=int(input("Enter a num:"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1




# 41 WAP to print sum of n natural num
# n=int(input("Enter a num:"))
# i=1
# total=0
# while i<=n:
#      total=total+i
#      i=i+1
# print(total)





# 42  WAP to find factorial of a num.
# n=int(input("Enter a num:"))
# fact=1
# i=1
# while (1,n+1):
#     fact=fact*i
#     print(fact)
    




#44 WAP to print all charactor of a string.

# s='Kailash'
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1



# 45.WAP to print all the charactors present at even index of a string.
# s="Kailash_Patel"
# i=1
# while i<len(s):
#     if i%2==0:
#         print(s[i])
#     i=i+1


#46 Wap to extract all lowercase charactor present in a string
# s="Kailash_Patel"
# low=' '
# i=0
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         low=low+s[i]
#     i=i+1
# print(low)


# 47.WAP to extract all vowel present in string.
# s="Kailash_Patel"   
# i=0
# while i<len(s):




# find HCF of given num:

# n1=int(input("Enter a num:"))
# n2=int(input("Enter a num:"))

# hcf=1
# i=1
# while i<n1:
#     if n1%i==0 and n2%i==0:
#         hcf=i
#     i=i+1
# print(hcf)





#  Extract all lowercases char from string using continue keyword.

# s="Kailash_Patel"

# res=''
# i=0
# while i<len(s):
#     if not 'a'<=s[i]<='z':
#         i=i+1
#         continue
#     res=res+s[i]
#     i=i+1
# print(res)


# Extract all even num in a list using continew keyword

# l=[2,3,4,5,6,7,8]
# even=[]
# i=0
# while i<len(l):
#     if l[i]%2 !=0:
#         i=i+1
#         continue
#     even.append(l[i])
#     i=i+1
# print(even)




# Extract only vowels from string using continue keyword.

# s="KailashPatel"
# out=''
# i=0
# while i<len(s):
#     if  not s[i] in "aeiou":
#         i=i+1
#         continue
#     out=out+s[i]
#     i=i+1
# print(out)



# Wap to print prime num.


# n=int(input("Enter a number:"))
# i=2
# for i in range(2,n):
#  while i<n:
#     if(n%i)==0:                        
#         print("Number is not prime")  
#         break  
#     i=i+1
# else:
#  print("Number is prime")




# WAP to num from 1 to 100 but if num divided by 7 and 9 then terminate the loop.

# i=1
# while i<=100:
#     if i%7==0 and i%9==0:
#         break
#     print(1)
#     i=i+1


# Create number guessing game



# k=" Kailash is student"
# a=k.split()
# print(a)


# s=["Hello","everyone"]
# out={"Hello":5 , "Everyone":8}

# out={}
# i=0
# while i<len(s):
#     out[s[i]]=len([i])
#     i=i+1
# print(out)


###############

# s="Power star".split

# out={"power":"rewop","Star":"rast"}

# i=0
# while i< len(s):
#     out[s[i]]=s[i][::-1]
#     i=i+1
# print(out)



# Reverse the string without using slicing

# s="kailash"
# rev="kai"
# i=0
# while i< len(s):
#     rev=s[i]+rev
#     i=i+1
# print(i)




# WAP  to get the following outputs.
# s=["kaislh.com","file.py","web.html","amazon.com","python.py"]
# out=['com','py']




# s=["kaislh.com","file.py","web.html","amazon.com","python.py"]

# out=['com','py']
# i=0
# while i< len(s):
#     ex=s[i].split(".")[-1]
#     if ex not in out:
#         out.append(ex)
#     i=i+1
# print(out)


# s=["kaislh.com","file.py","web.html","amazon.com","python.py"]

# out=['com','[kailsh']
# i=0
# while i< len(s):
#     it,ex=s[i].split(".")
#     if ex not in out:
#         out[ex]=[it]
#     else:
#         out[ex]+=[it]
#     i=i+1
# print(out)



