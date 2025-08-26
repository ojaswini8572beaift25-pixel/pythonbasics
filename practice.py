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

    elif(a=='%'):
        b=int(input("enter first number")) 
        c=int(input("enter second number"))
        print(b%c) 

    elif(a=='/'):
        b=int(input("enter first number"))
        c=int(input("enter second number"))
        print(b/c)

    elif(a=='*'):
        b=int(input("enter first number"))
        c=int(input("enter second number"))

    else:
        print("invalid input")    
        
