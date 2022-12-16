nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
somme = 0.0

# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = [0] * nombreEtudiants

for i in range(nombreEtudiants):
    notes[i] = float(input(f"Note étudiant {i} : "))
    somme = somme + notes[i]

moy = somme / nombreEtudiants
print(f"\nMoyenne de la classe : {moy}")

print("\nNuméro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moy
    print(f"{i} | {notes[i]} | {ecart}")