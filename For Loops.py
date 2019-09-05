#Task 14
#Compulsory Task 1


Num = int(input("Pleas enter a number:\t"))
print("The "+ str(Num) + " times table is:")


#becuase we want to print multiplication tables (multiples of 1->12) we start the loop at 1 and end at 13.
for i in range(1,13):  #we use 13 as the end index because the for loop will only count from 1 to (end index -1)
        print(str(Num) + " x " + str(i) + " = " + str(Num*i))



#Compulsory Task 2
print("")
Year = int(input("What year do you want to start with?\t"))
Year_Chk = int(input("How many years do you want to check?\t"))

# this loop we can start at 0 and end at the Year_Chk
print("")   #add new line for spacing and readability
for i in range(0,Year_Chk):
    if (Year%4 == 0):      #if year is a multiple of 4, then there will be no remainder when dividing by 4. therfore using "mod"
        print(str(Year) + " is a leap year")
    else:
        print(str(Year) + " isn't a leap year")

    Year +=1 # add 1 to the year so the loop will start checking again at the next year
        
