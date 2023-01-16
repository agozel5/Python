import re

def nettoyer_texte(texte):
    # Supprimer les caractères spéciaux, espaces et ponctuations
    texte = re.sub(r"[^a-zA-Z0-9]+", "", texte)
    # Remplacer les caractères accentués par leur caractère de base
    texte = texte.translate(str.maketrans("àáâãäåæçèéêëìíîïðñòóôõöøùúûüýÿ", "aaaaaaaceeeeiiiidnoooooouuuuyy"))
    # Passer le texte en minuscule
    texte = texte.lower()
    return texte

def est_palindrome(texte):
    # Nettoyer le texte
    texte = nettoyer_texte(texte)
    # Vérifier si c'est un palindrome
    return texte == texte[::-1]

texte = input("Entrez un mot ou une phrase : ")
if est_palindrome(texte):
    print("C'est un palindrome!")
else:
    print("Ce n'est pas un palindrome.")
