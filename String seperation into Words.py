#Task 17
#Compulsory Task 3


#String = "You must seperate this sentence into seperate words!"
String = input("Pleas enter a sentence:")
StringList = String.split()  #split the word into seperate pieces based on spaces.
#print(StringList)   

# the for loop will print the words in the stringList on seperate lines
for i in range(0, len(StringList)):
    print (StringList[i])

    #OR we cld use the ffg:
#for i in StringList:
#    print(i)
