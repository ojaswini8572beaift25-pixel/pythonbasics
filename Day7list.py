# A list in python is an ordered, mutable, indexed collection that allows duplicates.
# It is written in square brackets[].
# It can store mixed type of data (int,float,string,boolean etc.)

#print (my_list)

# my_list=[10,20,5,8.6,"Ojaswini"]

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

#Updating elements

# my_list[4]="Spiderman"
# print(my_list)

#Adding elements
# my_list.append("Done")

# my_list.insert(2,40)
# print(my_list)

#Removing elements
# my_list.remove(40)
# print(my_list)
# del my_list[4]
# print(my_list)
# print(len(my_list))

#Sorting list in ascending order

# nums=[9,3,2,1,9,10,15,17]
# nums.sort()
# print("the list in ascending order is ;",nums)

# #Sorting list in descending order

# nums=[9,3,2,1,9,10,15,17]
# nums.sort(reverse=True)
# print("the list in descending order is :", nums)

# printing with index 

# nums=[5,3,2,1,9,10,15,17]
# print(nums[0:6:2])
# here 0= starting index value
#      6= ending index value
#      2= gap in list jo chalega compiller

#To find second largest number in a list

# def second_largest(nums):
#     a=list(set(nums))
#     a.sort()
#     if len(a)<2:
#      return None
#     return a[-2]

# nums=[10,20,4,45,78,99,20,34,78]
# print("second largest is :", second_largest(nums))

#to reverse a list

# def reverse_list(ist):
#    return ist[:: -1]
# nums=[1,2,3,4,5]
# print ("reverse is:",reverse_list(nums))

#To find a pair of digits that make up a given sum 

# def findpairs(ist,target):
#     pairs=[]
#     for i in range(len(ist)):
#         for j in range(i+1, len(ist)):
#             if ist[i]+ist[j]==target:
#                 pairs.append((ist[i],ist[j]))
#     return pairs

# nums=[1,5,7,-1,5]
# target=6
# print("Pairs with sum", target," ", findpairs(nums,target)) 


