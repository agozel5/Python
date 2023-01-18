import re

def nettoyer_texte(texte):
    texte = re.sub(r"[^a-zA-Z0-9]+", "", texte)
    texte = texte.translate(str.maketrans("àáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ", "aaaaaaaceeeeiiiidnoooooouuuuyy"))
    texte = texte.lower()
    return texte

def est_palindrome(texte):
    texte = nettoyer_texte(texte)
    return texte == texte[::-1]

texte = input("Entrez un mot ou une phrase : ")
if est_palindrome(texte):
    print("C'est un palindrome!")
else:
    print("Ce n'est pas un palindrome.")
