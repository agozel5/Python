notes = []
coefficients = []
for i in range(5):
    s = input("Veuillez entrer la note du module " + str(i+1) + " et le coefficient correspondant : ")
    s = s.split(" ")
    notes.append(float(s[0]))
    coefficients.append(int(s[1]))

total_coefficients = sum(coefficients)
total_notes = 0
for i in range(5):
    total_notes += notes[i] * coefficients[i]

average = total_notes / total_coefficients

if average > 10:
    if min(notes) >= 8:
        print("Admis avec une moyenne de", average)
    else:
        print("Refusé car une note est inférieure à 8")
else:
    print("Refusé avec une moyenne de", average)