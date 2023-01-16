notes = []
coefficients = []
for i in range(5):
    s = input("Veuillez entrer la note du module " + str(i+1) + " et le coefficient correspondant : ")
    s = s.split(" ")
    notes.append(float(s[0]))
    coefficients.append(float(s[1]))

total_coefficients = sum(coefficients)
total_notes = 0
for i in range(5):
    total_notes += notes[i] * coefficients[i]

average = total_notes / total_coefficients

if average > 10:
    if min(notes) >= 8:
        print("L'étudiant est admis avec une moyenne de", average)
    else:
        print("L'étudiant est refusé car une note est inférieure à 8")
else:
    print("L'étudiant est refusé avec une moyenne de", average)
