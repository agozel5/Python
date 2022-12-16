nMax = 10
v1 = []
v2 = []
n = 0
scalaire = 0
while n < 1 or n > nMax :
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10]?"))

print("\nSaisie du premier vecteur:")
for i in range(n):
    v1.append(float(input(f"v1[{i}]=")))

print("\nSaisie du premier vecteur:")
for i in range(n):
    v2.append(float(input(f"v1[{i}]=")))

for i in range(n):
    scalaire = scalaire + v1[i] * v2[i]

print(f"\nLe produit scalaire de v1 par v2 vaut {scalaire}")