iban = input("Enter IBAN, please: ") # ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability...
iban = iban.replace(' ','') #  ...but remove them immediately)
if not iban.isalnum(): # the entered IBAN must consist of digits and letters only - if it doesn't...
    print("You have entered invalid characters.") # ...output the message;
elif len(iban) < 15: #  the IBAN mustn't be shorter than 15 characters (this is the shortest variant, used in Norway)
    print("IBAN entered is too short.") # if it is shorter, the user is informed;
elif len(iban) > 31: # moreover, the IBAN cannot be longer than 31 characters (this is the longest variant, used in Malta)
    print("IBAN entered is too long.") # if it is longer, make an announcement;
else: # start the actual processing;
    iban = (iban[4:] + iban[0:4]).upper() # move the four initial characters to the number's end, and convert all letters to upper case (step 02 of the algorithm)
    iban2 = '' # this is the variable used to complete the number, created by replacing the letters with digits (according to the algorithm's step 03)
    for ch in iban: # iterate through the IBAN;
        if ch.isdigit(): # if the character is a digit... 
            iban2 += ch # just copy it;
        else: # otherwise...
            iban2 += str(10 + ord(ch) - ord('A')) # ...convert it into two digits (note the way it's done here)
    ibann = int(iban2) # the converted form of the IBAN is ready - make an integer out of it;
    if ibann % 97 == 1: # is the remainder of the division of iban2 by 97 equal to 1?
        print("IBAN entered is valid.") #  If yes, then success;
    else: # Otherwise...
        print("IBAN entered is invalid.") # ...the number is invalid.