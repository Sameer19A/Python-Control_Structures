#Task 10
#Optional Task


Weight = float(input("Please enter your weight in kg's:\t"))
Height = float(input("Please enter your height in m:\t"))

BMI = Weight / (Height*Height)
BMI = round(BMI,2)

if (BMI>=30):
    print("Your BMI is: " + str(BMI) +". You are obese!")

elif (BMI>=25):
    print("Your BMI is: " + str(BMI) +". You are oveweight!")

elif (BMI>=18.5):
    print("Your BMI is: " + str(BMI) +". You are normal!")

else:
    print("Your BMI is: " + str(BMI) +". You are underweight!")


    
