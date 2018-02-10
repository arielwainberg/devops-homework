#2- Strings are also lists:
#Because strings are lists, you can do to strings everything that you do to lists. You can iterate through them:
#string = "example"
#for c in string:
#    print ("one letter: " + c)
#Write a Python function that counts the vowel letters (a,e,i,o,u)  in a given string!

def vowelcheck(word):
    vowel_letters = ["a","e","i","o","u"]
    vowelcount=0
    for c in word:
        if c in vowel_letters:
            vowelcount += 1
    print(f"in the word '{word}', there are {vowelcount} vowel letters ")
wordtocheck = input("Please type the word you want to check: ")
vowelcheck(wordtocheck)