
# rows=5
# for i in range(1,rows+1):
#     for j in range(i):
#         print("1",end=" ")
#     print()
   
# rows=5
# for i in range(1,rows+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()    

# rows=10
# num=1
# for i in range(1,rows+1):
#     for j in range(i):
#      print(num,end=" ")
#      num+=1
#     print()   

# rows=5
# for i in range(rows,0, -1):
#     for j in range(i):
#         print("*",end=" ")  
#     print()

n=int(input("enter number"))
for i in range(1,n+1):
    for j in range(1,n+1):
           if(j<=n-i):
            print(" ", end=" ")
           else:
             print("*",end=" ")
    print()       
    