import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return len([x for x in table if x < vseuil])

nb = int(input("Combien de valeurs voulez-vous générer? "))
vmin = int(input("Valeur minimale? "))
vmax = int(input("Valeur maximale? "))
print(f"Générer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
seuil = input("Voulez-vous préciser le seuil? (O/N) ")
if seuil.upper() == "O":
    vseuil = int(input("Seuil? "))
else:
    vseuil = 30
total = combienInferieur(tab, vseuil)
print(f"Il y en a {total} inférieurs à {vseuil}")
