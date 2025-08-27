a=int(input("enter number"))
count = 0

while a != 0:
    a //= 10 
    count += 1

print("Number of digits :",count)
