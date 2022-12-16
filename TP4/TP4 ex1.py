n = float(input("Vous cherchez la table de multiplication de quel nombre?"))
l=[]
for i in range(10):
    l.append(round(n*i,1))
    print(f"{n}*{i}={l[i]}")