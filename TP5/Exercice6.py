def Char():
    T = input("Entrez une chaîne de caractères : ")

    taille_T = 0
    for caractere in T:
        taille_T += 1
    print(f"La taille de la chaîne T est : {taille_T}")

    voyelles = "aeiouyAEIOUY"
    nombre_voyelles = 0
    for caractere in T:
        if caractere in voyelles:
            nombre_voyelles += 1

    pourcentage_voyelles = nombre_voyelles / taille_T * 100
    print(f"Le pourcentage de voyelles dans T est : {pourcentage_voyelles}%")

    position_wagon = -1
    for i in range(taille_T - 4):
        if T[i] == "w" and T[i + 1] == "a" and T[i + 2] == "g" and T[i + 3] == "o" and T[i + 4] == "n":
            position_wagon = i
            break
    if position_wagon != -1:
        print(f"La chaîne 'wagon' est une sous-chaîne de T, elle commence à la position {position_wagon}")
    else:
        print("La chaîne 'wagon' n'est pas une sous-chaîne de T.")

    occurrences_wagon = 0
    for i in range(taille_T - 4):
        if T[i] == "w" and T[i + 1] == "a" and T[i + 2] == "g" and T[i + 3] == "o" and T[i + 4] == "n":
            occurrences_wagon += 1
    print(f"Il y a {occurrences_wagon} occurrences de la chaîne 'wagon' dans T.")
Char()