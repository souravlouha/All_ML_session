#STRING
name = "sourav"

print(len(name)) # string ar lenth bolbe , mane kotogulo character ache


print(name.endswith("av")) # string ar ses ,mane end ki diye hochhe , seta bolbe ; True False ar modhhome result show korbe 
# True : name se 'av' diye end hochhe
print(name.endswith("va"))
# False : name se 'av' diye end nai hochhe

print(name.startswith("so"))                    
print(name.startswith("su")) 
## string ar suru ,mane start ki diye hochhe , seta bolbe 



#Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input ("Enter your name:")
print(f"Good Afternoon {name}") # f representing fstring 


#Write a program to fill in a letter template given below with name and date. letter = ''' Dear <|Name|>, You are selected! <|Date|> '''

letter = ''' Dear <|Name|>, You are selected! <|Date|> '''

print(letter.replace("<|Name|>","Sourav").replace("<|Date|","18 jan 2025"))



#Write a program to detect double space in a string.
name = "Soumita is a good  girl and  "
print(name.find("  "))

#STRING SLICING