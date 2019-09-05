haveLength = False
upCase = False
LowCase = False
haveNum = False
i = 0    # i is a count used to count the number of Yes's

Length = input("Is the length of your password atleast 6 characters long? Yes/No\t")
Uppercase = input("Does your password contain uppercase letters? Yes/No\t")
Lowercase = input("Does your password contain lowercase letters? Yes/No\t")
Numchk = input("Does your password contain numbers? Yes/No\t")

if Length.lower() == "yes" :
    haveLength = True
    i +=1

if Uppercase.lower() == "yes":
    upCase = True
    i +=1

if Lowercase.lower() == "yes":
    LowCase = True
    i +=1

if Numchk.lower() == "yes":
    haveNum = True
    i +=1

if i>=3:     # if i is >= 3, then 3 conditions have been met and therefore password is suitable
    print("\nThis is a suitable password!")
else:
    print("\nYour password is not suitable!")
