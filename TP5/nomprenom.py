# Demande d'entrée le nom de la première personne
nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

# Nom de la deuxième personne
nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

# Formatage
nom1 = nom1.upper()
prenom1 = prenom1.capitalize()
nom2 = nom2.upper()
prenom2 = prenom2.capitalize()

# Compare
if nom1 < nom2:
  print(prenom1, nom1)
  print(prenom2, nom2)
elif nom1 > nom2:
  print(prenom2, nom2)
  print(prenom1, nom1)
else: # compare prénom si nom sont égaux
  if prenom1 < prenom2:
    print(prenom1, nom1)
    print(prenom2, nom2)
  else:
    print(prenom2, nom2)
    print(prenom1, nom1)

