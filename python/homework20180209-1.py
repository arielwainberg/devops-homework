#1- Take a list, for example:
#      [4, 2 , 7 , 8, 9, 10, 2, 8, 6]
#
## A- Write a Python function that calculates the Sum of the list
## B- Write a Python function that calculates the Average of the list
##########################[==A==]####################################
#numlist = [4, 2 , 7 , 8, 9, 10, 2, 8, 6]
#summary = 0
#for num in numlist:
#    summary = num + summary
#print(summary)
#####################################################################
###########################[==B==]###################################
numlist = [4, 2 , 7 , 8, 9, 10, 2, 8, 6]
summary = 0
count = 0
for num in numlist:
    count = count + 1
    summary = num + summary
avarage = summary // count
print (f"Summary of all the numbers in you list is :{summary}")
print (f"Count of numbers in the list is: {count}")
print(f"The numbers avarage in the list is: {avarage}")