# Initialisation de la liste
L1 = [0]*3

# Affichage de la liste, de son type et de son id
print(L1)
print(type(L1))
print(id(L1))

# Boucle pour afficher le type et l'id de chaque élément
for i in range(len(L1)):
    print(f"Type of element at index {i}: {type(L1[i])}")
    print(f"Id of element at index {i}: {id(L1[i])}")

# Modification de l'élément en deuxième position
L1[1] += 1

# Affichage de la liste, de son type et de son id après modification
print(L1)
print(type(L1))
print(id(L1))

# Boucle pour afficher le type et l'id de chaque élément après modification
for i in range(len(L1)):
    print(f"Type of element at index {i}: {type(L1[i])}")
    print(f"Id of element at index {i}: {id(L1[i])}")
