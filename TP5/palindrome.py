import re

def is_palindrome(string):
    string = re.sub(r'[^A-Za-z]', '', string)
    string = string.lower()
    return string == string[::-1]

string = input("Entrez un mot ou une phrase : ")
if is_palindrome(string):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")

 # Ce programme élimine les caractères non alphabétiques puis converti en minuscules et finalement teste si la chaîne est un palindrome
