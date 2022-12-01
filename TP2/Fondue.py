Base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConv=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromage = (fromage*nbConv)/Base
eau = (eau*nbConv)/Base
ail = (ail*nbConv)/Base
pain = (pain*nbConv)/Base


print("Pour faire une fondue fribourgeoise pour",nbConv," personnes, il vous faut :")
print("-",fromage,"g de fromage")
print("-",eau,"dl eau")
print("-",ail,"gousses d'ail")
print("-",pain,"gr de pain")