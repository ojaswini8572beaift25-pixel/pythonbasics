#Fibonacci series upto n terms using for loop

n=int(input("enter number of terms: "))
a=0
b=1
print("Fibonacci series: ")
for i in range(n):
    print(a)
    a,b=b,a+b 