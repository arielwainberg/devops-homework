#3- Write a Python program that receives the Name of the user and his age,
#then prints the Name and on which year he/she will reach the age of 120!
#To get user input use the input function
#name = input('Please enter your name:')
import datetime
now = datetime.datetime.now()
currentyear = now.year
dstage = 120 
name = input("What is your name? ")
age = input("How old are you? ")
calculate = dstage - int(age) +int(currentyear)
print(f"{name}, at year {calculate}, you will be {dstage} years old")
