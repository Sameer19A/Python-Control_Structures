#Compulsory Task 1:

Price = float(input("Pleas enter the price of the item you would like to purchase:\t"))
Distance = float(input("Please enter the total distance of the delivery in km's:\t"))


print ("\n Now please select your delivery method: ")
Air_Freight = input("\n Would you like Air or Freight delivery?\t")
Insurance =  input("\n Would you like Full or Limited insurance?\t")
Gift =  input("\n Would you like to add a gift? Yes/No\t")
Del_Type =  input("\n Would you like Priority or Standard delivery?\t")

if Air_Freight.lower() == "air" :
    A_F_Cost = Distance*0.36     # Cost of shipping by air

else:
    A_F_Cost = Distance*0.25     # Freight cost


if Insurance.lower() == "full":
    Ins_Cost = 50.00            #Cost of Full Insurance

else:
    Ins_Cost = 25.00            #Cost of Limited Insurance


if Gift.lower() == "yes":
    Gift_Cost = 15.00           #cost of adding a gift

else:
    Gift_Cost = 0.00

if Del_Type.lower() == "priority":
    Type_Cost = 100.00          #Cost of Priority delivery

else :
    Type_Cost = 20.00


Total_Cost = Price + A_F_Cost + Ins_Cost + Gift_Cost + Type_Cost

print("\nThe total cost of the package is:\tR" + str(Total_Cost))
