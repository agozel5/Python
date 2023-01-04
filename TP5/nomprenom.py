# Nom/ Prénom 1er personne
nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

# Nom/ Prénom 2ème personne
nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

# Formatage
nom1 = nom1.upper()
prenom1 = prenom1.capitalize()
nom2 = nom2.upper()
prenom2 = prenom2.capitalize()

# On compare les noms et on affiche les prénoms et les noms dans l'ordre alphabétique
if nom1 < nom2:
  print(prenom1, nom1)
  print(prenom2, nom2)
elif nom1 > nom2:
  print(prenom2, nom2)
  print(prenom1, nom1)
else: # Si les noms sont égaux, on compare les prénoms
  if prenom1 < prenom2:
    print(prenom1, nom1)
    print(prenom2, nom2)
  else:
    print(prenom2, nom2)
    print(prenom1, nom1)

