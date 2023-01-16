def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

# Initialisation de la liste lst1
lst1 = [0, 1, 2]

# Initialisation de la liste lst2
lst2 = ajouter_elt(lst1, len(lst1))

# Affichage de la liste lst1, de son type et de son id
print(lst1)
print(type(lst1))
print(id(lst1))

# Affichage de la liste lst2, de son type et de son id
print(lst2)
print(type(lst2))
print(id(lst2))
