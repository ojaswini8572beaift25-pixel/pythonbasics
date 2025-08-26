# print first 10 natural numbers
# for i in range(1,11):
#     print(i)  

  
#print even numbers from 1 to 100
# i=2
# while(i<=100):
#     print(i)
#     i=i+2


#print squares of 1 to 10
# n=1
# while n<=10:
#     print("square of",n,"is",n*n)
#     n=n+1


#print sum of n natural numbers
# num=int(input("enter number"))
# if num<0:
#     print("enter positive number")
# else: 
#     sum=0
#     while num>0:
#         sum +=num
#         num -= 1

#     print(sum)  


#print multiplication table of 3
# a=int(input("enter number"))

# for i in range(1,11):
#     print((f"{a}*{i}={a*i}"))


#print factorial of number using for loop

# num=int(input("enter number :"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("Factorial of ",num,"is :",fact) 


#Fibonacci series upto n terms using for loop

n=int(input("enter number of terms: "))
a=0
b=1
print("Fibonacci series: ")
for i in range(n):
    print(a)
    a,b=b,a+b 