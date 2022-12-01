temp=int(input("nombre de minute écoulées:"))
jour=temp//(24*60)
heure=int(temp/60)-jour*24
minute=temp-heure*60-jour*24*60
print(f"il y a {jour} jours qui sont passés et {heure} heures et {minute} minutes qui se sont écoulées.")