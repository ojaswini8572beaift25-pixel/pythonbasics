#  Write a program that takes two numbers as input and prints their sum, difference, product, and division.

while True:
    print("select from the following operations + , - , % , / , *")
    print("press $ to exit")
    a=input()
    if(a=="$"):
        break

    elif(a=='+'):
        b=int(input("enter first number"))
        c=int(input("enter second number"))
        print(b+c)

    elif(a=='-'):
        b=int(input("enter first number"))
        c=int(input("enter second number"))
        print(b-c)


    elif(a=='/'):
        b=int(input("enter first number"))
        c=int(input("enter second number"))
        
        print(b/c) 

    elif(a=='*'):
        b=int(input("enter first number"))
        c=int(input("enter second number"))
        print(b*c)

    else:
        print("not right") 

           










# if b != 0:
#             div_result= b/c
#         else: 
#             div_result= "undefined"

        
# elif(a=='%'):
#         b=int(input("enter first number")) 
#         c=int(input("enter second number"))
#         print(b%c) 