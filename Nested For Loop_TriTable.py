#Task 15
#Compulsory Task

PyrRow = 10   # PyrRow is the numebr of rows in the pyramid plus 1
for R in range(1,PyrRow):        #R is the row number
    for C in range(1,(r+1)):     #C is the coloumn number

        #printing the pyramid - values to print change according to the outer loop (row)
        print( str(R*C)+"\t",end="")  #prints r*c for c from 1 to (r+1)


    print("")  #prints a new line after each row
