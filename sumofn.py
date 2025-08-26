#print sum of n natural numbers

num=int(input("enter number"))
if num<0:
    print("enter positive number")
else: 
    sum=0
    while num>0:
        sum +=num
        num -= 1

    print(sum)  
