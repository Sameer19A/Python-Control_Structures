#Task 17
#Compulsory Task 1
#This program reads in a string and makes each alternate character an Uppercase character and each other alternate character a lowercase character.
String = "This string is the testing string"

#to find each alternate character, we use a for loop
for i in range(0,len(String)):
    #if the character has an even position number(i) it will not have a remainder.
    if i%2 == 0:   # even character position -make uppercase
        StringChar = String[i].upper()
        print(StringChar,end="")
    else:
        StringChar = String[i].lower()
        print(StringChar,end="")


