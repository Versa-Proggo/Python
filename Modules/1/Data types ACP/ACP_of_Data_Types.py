#Concatenation
var1 = "Versa"
var2 = "Proggo"
print(f"The variables together are: {var1 +var2}")

#Indexing a string
variable_string = "Sthitoproggo Noirrit A.K.A Versa_Proggo"
print({variable_string [::3]})
print({variable_string [0::1]})
print({variable_string [::-1]})

#Upper Case
word = input("Enter a word: ")
word2 = word[0].upper() + word[1:]
print(f"{word} with the first letter capitalized is {word2}")