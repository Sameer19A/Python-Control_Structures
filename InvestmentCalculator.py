#Task 12
#Compulsory Task 1

import math         #import must always be the first line


print("Investment Calculator")

P = float(input("Please enter the amount you would like to deposit:\t"))
i = float(input("Please enter the interest rate:\t"))
t = float(input("Please enter the number of years you would like to invest for:\t"))
interest = input("Would you like to earn simple or compound interest on your investment?\t")

r = i/100

if interest.lower() == "simple":
    A = P*(1+r*t)

elif interest.lower() == "compound":
    A = P * math.pow((1+r),t)
    A = round(A,2)

else:
    print("You have not selected an investment type!")


print("Your investment will be worth R" + str(A) + " after " + str(t) + " years!")
