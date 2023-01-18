def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]
lst2 = ajouter_elt(lst1, len(lst1))

# Affichage du type et id: liste 1
print(lst1)
print(type(lst1))
print(id(lst1))

# Affichage du type et id :liste 2
print(lst2)
print(type(lst2))
print(id(lst2))
