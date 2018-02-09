#2- Strings are also lists:
#Because strings are lists, you can do to strings everything that you do to lists. You can iterate through them:
#string = "example"
#for c in string:
#    print ("one letter: " + c)
#Write a Python function that counts the vowel letters (a,e,i,o,u)  in a given string!

string = "authorization"
vowel = ["a", "e", "i", "o", "u"]
x = 0
for a in string:
    for b in vowel:
        if b == a:
            x = x + 1
print(f"'{string}' word has {x} vowel letters")


