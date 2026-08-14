# 11.wap to check data is mutable or not.

# data=eval(input("Enter your data:"))
# if type(data) in[list,set,dict]:
#     print("data is mutable.")
# else:
#     print("data is immutable.")




# 12.WAP to given charactor is digit or not

# data=eval(input("enter your string."))
# if 0<= data <=9:
#     print(data,"is digit.")
# else:
#     print(data,"not digit.")


# 13.WAP to given char is special or not

# ch=eval(input("enter data:"))
# if 'a'<= ch <='z' or 'A'<=ch<='Z' or 0 <= ch <=9:
#     print(ch,"is  not special.")
# else:
#     print(ch," special digit.")




#14 WAP to check whether a list consists of middle value or not.
# l=[True,5,'bye',False,5.6]

# if len(l)%2!=0:
#     print("have mid value.")
# else:
#     print(l,"not containing middle value.")



# WAP to check whether 2 value are pointing 


# a=359
# b=359
# if a is b:
#     print("yes")
# else:
#     print("No")




# WAP to check num is positive or negative

# num=int(input("enter a num:"))
# if num>0:
#     print("num is positive.")
# else:
#     print("num is negative.")







# WAP to check string is polindrom or not.

# # s=input("enter string.")
# if s==s[::-1]:
#     print("string is palindrome.")
# else:
#     print("string is not palindrome.")
    





# Number Guessing Game

import random

# Generate a random number between 1 and 100

secret_number = random.randint(1, 50)

print("Guess the number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low! Try Again.")
    elif guess > secret_number:
        print("Too High! Try Again.")
    else:
        print(f"Congratulations! You guessed the correct number {secret_number}.")
        break


















