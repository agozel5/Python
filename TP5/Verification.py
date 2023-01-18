import os
import datetime

# demande: noms de deux fichiers à l'utilisateur
file1 = input("Entrez le nom du premier fichier : ")
file2 = input("Entrez le nom du deuxième fichier : ")

# vérifier fichiers existent
if os.path.isfile(file1) and os.path.isfile(file2):
    # afficher la taille des fichiers en octets
    print("Taille de " + file1 + " : " + str(os.path.getsize(file1)) + " octets")
    print("Taille de " + file2 + " : " + str(os.path.getsize(file2)) + " octets")

    #  fichier le plus récent en comparant les timestamps de modification
    file1_mtime = os.path.getmtime(file1)
    file2_mtime = os.path.getmtime(file2)
    if file1_mtime > file2_mtime:
        recent_file = file1
        recent_mtime = file1_mtime
    else:
        recent_file = file2
        recent_mtime = file2_mtime

    # formatage de la date la plus récente
    recent_date = datetime.datetime.fromtimestamp(recent_mtime)
    print("Le fichier le plus récent est " + recent_file + " modifié le " + recent_date.strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("Au moins un des fichiers spécifiés n'existe pas.")
