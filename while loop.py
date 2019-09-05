#Task 13 - While loops
#Compulsory Task 1

SumNum = 0
i = 0   # i is a counter to count the number of times the user entered a valid number

#First ask the user to enter a number
UserNumber = int(input("Please enter a number:\t"))

#We ask the user to enter a number first and the while loop below will execute as long as the user entered a number that is !=-1
#if the user entered an accepted number, we immediately add it to the total sum and incerase the count.
#After increasing the count, we ask the user to enter another number, then the loop executes again as long as that number is !=-1

while UserNumber !=-1 :   
    SumNum += UserNumber    # add the users number to Sum
    i += 1   # add 1 to the counter i 
    UserNumber = int(input("Please enter a number:\t"))   

#print(str(SumNum))   #use this print statement to check the loop is adding the entered numbers correctly
#print(str(i))         #check the count of the correclty entered numbers 

if i>0 :
    Average = round(SumNum/i,2)
    print("\nThe average of the numbers entered is " + str(Average))





#Compulsory Task 2
print("\n\nCompulsory Task 2: ")

UserName = input("\nPlease enter your name:\t")
i = 0   #count the number of incorrect tries
while UserName != "Sameer":
    i+= 1       #inc count
    if UserName == "Exit":      #if the user enters the word Exit, we make username equal Sameer which will also stop the while loop when it tried to run again
        UserName = "Sameer"     #username = Sameer will stop the while loop
        i = 0
    else:
        UserName = input("Please enter your name:\t")


if i>0:
    print("It took " + str(i) + " tries but you finally got it right! :)")
