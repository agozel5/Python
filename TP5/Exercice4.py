montant = int(input("Entrez le montant d'argent : "))
billets = [100, 50, 10]
pieces = [2, 1]

for billet in billets:
    nombre = montant // billet
    montant -= nombre * billet
    print(f"c'est donc {nombre} billets de {billet}")

for piece in pieces:
    nombre = montant // piece
    montant -= nombre * piece
    print(f"c'est donc {nombre} pièces de {piece}")
