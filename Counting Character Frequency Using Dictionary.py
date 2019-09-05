#Task 17
#Compulsory Task 2

print("Counting the character frequency in a string: \n")

String =input("Enter a string:\t")

Chars = {}   # this is a dictionary called Chars which will store the characters counted as well as the character frequency

for n in range(0,len(String)):  # for each character (n) in the user entered string, do the ffg:
    Current_Char = String[n]   # make the current char = to the String at pos n
    freq = 0  #new freq count
    Freq = 0  #existing Freq count in the dictionary that needs to be updated if the character already exists.
    if Current_Char in Chars:   #if character exists in the dictionary, find the index of that character, then increase the frequency count. else add to the list and increase freq count by 1
        Freq = Chars[Current_Char]    #make the existing Freq count equal to the value that matches the key(current_Char)
        Freq += 1                   #increase the existing frequency count
        Chars[Current_Char]=Freq   #change the value of the Current_Char to the new Freq count

    else:   # if the character does not exist in the dictionary -add it
        freq+=1
        Chars[Current_Char] = freq #adds the character and frequency to the dictionary

    
print("")
print(Chars)   # prints the dictionary Chars


