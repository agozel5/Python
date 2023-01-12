def calculer_salaire():
    heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
    salaire_horaire = int(input("Entrez le salaire horaire : "))

    salaire = 0
    if heures_travaillees <= 160:
        salaire = heures_travaillees * salaire_horaire
    elif heures_travaillees <= 200:
        salaire = 160 * salaire_horaire + (heures_travaillees - 160) * (salaire_horaire * 1.25)
    else:
        salaire = 160 * salaire_horaire + 40 * (salaire_horaire * 1.25) + (heures_travaillees - 200) * (salaire_horaire * 1.5)
    return salaire

print(f"le salaire de l'ouvrier est {calculer_salaire()}") 