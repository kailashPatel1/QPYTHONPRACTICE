## For Loop:  it is self iterative loop 
# note: initilizatin and updation is not mendetory in for loop
# we can use for loop on every collection data types exam: string, list, tuple, set,Dictionary, range

# Syntax:   for var in collection
                # code to execution 



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
