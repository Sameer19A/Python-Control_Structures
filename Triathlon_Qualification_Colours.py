#Task 11
#Compulsory Task 1

print("Qualifying times for a triathlon:")

QT = float(input("Please enter the required Qualifying time (in minutes):\t"))

SwimTime = float(input("Please enter the qualifying time (in minutes) for Swimming:\t"))
CyclingTime = float(input("Please enter the qualifying time (in minutes) for Cycling:\t"))
RunTime = float(input("Please enter the qualifying time (in minutes) for Running:\t"))


Total_Time = SwimTime + CyclingTime + RunTime

if Total_Time < QT :
    Award = "Provincial Colours"
    
elif (Total_Time > QT) and (Total_Time < (QT + 5)):     #Within 5 mins of QT meaning 5 mins above QT
    Award = "Provincial Half Colours"

elif (Total_Time > (QT + 5)) and Total_Time < (QT + 10):     #Within 10 mins of QT meaning 10 mins above QT
    Award = "Provincial Scroll"

else:
    Award = "Provincial Certificate"


print("\nYour total time is " + str(Total_Time) + " minutes and you have been awarded " + Award)
