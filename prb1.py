name = "Zearin: "              #input
vowels = 0                     #initialize counters
consonants =0                  #initialize counters
for ch in name:                #using for loop for the characters and store in ch
    if ch in  "aeiouAEIOU":    #check the character is a vowel 
        vowels += 1            #increment the vowel counter by 1.
    elif ch.isalpha(): 
        consonants += 1        #increment the consonants counter by 1.

print("Number of vowels:", vowels)
print("number of consonants: ", consonants)