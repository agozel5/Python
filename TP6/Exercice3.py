def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

#a)
print(ajouter_elt()) #affiche [0,1,2,3]

#b)
print(ajouter_elt()) #affiche [0,1,2,3]
print(id(ajouter_elt())) #affiche l'id de la liste retournée par la fonction
# La fonction retourne la même liste avec les mêmes valeurs pour les deux appels car c'est la même instance de la liste qui est utilisée en mémoire

#c)
def ajouter_carac(ch='abc', elt='d'):
    return ch + elt

#d)
print(ajouter_carac()) #affiche 'abcd'

#e)
print(ajouter_carac()) #affiche 'abcd'
print(id(ajouter_carac())) #affiche l'id de la chaine retournée par la fonction
# La fonction retourne la même chaine avec les mêmes valeurs pour les deux appels car c'est la même instance de la chaine qui est utilisée en mémoire
