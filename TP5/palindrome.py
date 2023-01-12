import re

def is_palindrome(string):
    # éliminer les caractères non alphabétiques
    string = re.sub(r'[^A-Za-z]', '', string)
    # convertir en minuscules
    string = string.lower()
    # tester si la chaîne est un palindrome
    return string == string[::-1]

string = input("Entrez un mot ou une phrase : ")
if is_palindrome(string):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")

