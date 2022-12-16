while True:
    date = input("Entrez une date sous forme jjmmaaaa : ")

    d = int(date[0] + date[1])
    r = int(date[2] + date[3])

    j = str()
    for i in range(4, len(date)):
        j = j + date[i]
    j = int(j)

    if r == 2:
        if (((j % 4) != 0) | ((j % 100) == 0) | ((j % 400) != 0)) & (d > 28):
            print(f"La date est fausse, il n'y a que 28j dans le mois de février de l'année {j}")
        elif d > 29:
            print(f"La date est fausse, il n'y a que 29j dans le mois de février de l'année {j}")
        else:
            print(f"La date {d}/{r}/{j} est correcte")
            break
    elif (r > 12) | (d > 31):
        print("La date est fausse, un mois ne peut contenir plus que 31j")
    elif (1 <= r <= 7) & (r % 2 == 0) & (d > 30):
        print("La date est fausse, il n'y a que 30j dans le mois indiqué")
    elif (8 <= r <= 12) & (r % 2 != 0) & (d > 30):
        print("La date est fausse, il n'y a que 30j dans le mois indiqué")
    else:
        print(f"La date {d}/{r}/{j} est correcte")
        break