#Task 17
#Compulsory Task 4

String = input("Please enter a string:\t")
Remove = input("Which characters would you like to make dissappear:\t")

for n in range(0,len(Remove)):   # count the number of characters the user wants to remove
    String = String.replace(Remove[n],"")   # loop through the string and remove the character that matches the character entered in the Remove string (Remove[n]) with the space("")
print(String)