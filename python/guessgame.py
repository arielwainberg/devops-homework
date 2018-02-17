import random
rndnum = random.randint(1,9)
print(rndnum)
a = int(input("Try to guess the number I have randomized: "))
while a != rndnum:
    if a == rndnum:
        print(f"Exelent, you have guessed the randomize number, the number was {rndnum}")
        break
    elif a > (rndnum):
        print(f"The number '{a}' is Higher than the ranndomize number, try lowest number ")
    elif a < (rndnum):
        print(f"The number '{a}' is lower than the ranndomize number, try higher number ")
    a = int(input("take another try, your guess ?"))