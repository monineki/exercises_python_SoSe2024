wort = "Hallo, Berl%&"

letter_count = 0
    
for buchstaben in wort:
    if buchstaben.isalpha():
        letter_count += 1
            
print ( letter_count)



def buchstaben_zählen(wort):
 
    letter_count = 0   
    for buchstaben in wort:
        if buchstaben.isalpha():
            letter_count += 1
            
    return letter_count
      
print(buchstaben_zählen("Hallo, B3erl%&g"))



