x = int(input("Entrez un nombre entier:"))
if x > 0:
    if x % 2 ==0:
        print("paire et positif")
    if x % 2 ==1:
        print("Le nombre est impaire et positif")

if x < 0:
    if x % 2 ==0:
        print("Le nombre est paire et negatif")
    if x % 2 ==1:
        print("Le nombre est impaire et negatif")

if x ==0:
    print("Le nombre est paire et nul")