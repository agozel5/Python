jour = int(input("donne jour:"))
heure = int(input("donne heure:"))
minute = int(input("donne minute:"))

if jour > 31 or jour < 0:
    jour=int(input("donne jour:"))
if heure > 24 or heure < 0:
    heure = int(input("donne heure:"))
if minute >60 or minute < 0:
    minute = int(input("donne minute:"))

print(minute+(heure*60)+(jour*1440))