# -*- coding: utf-8 -*-
"""
TP NSI 1ére Générale 2022-2023
José ARAUJO
Créez 2 listes
"""

# L'exercice il fonctionne

print("Ex1:")
joursOuvres = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
weekEnd = ["samedi", "dimanche"]
semaine = list(joursOuvres + weekEnd)
print("joursOuvres:\nqq", joursOuvres)
print("weekEnd:\n", weekEnd)
print("semaine:\n", semaine) 

print()
print("*" * 7 + " END " + "*" * 7)
print()
"""
Question 2:
Utiliser "pop" et "insert" pour modifier la liste semaine
afin que la semaine commence le dimanche
"""
# Le script il fonctionne
# semaine.insert(0, semaine.pop(6))
print("Ex2:")

# J'ai utilisé une boucle pour vérifier si le premier element de ma liste
# est le dimanche, tant qu'il ne l'est pas, la boucle ne l'arretera pas.
# Dans la boucle j'ajoute le dernier element au début de la liste.

while semaine[0] != "dimanche":
    semaine.append(semaine.pop(0))

print(semaine) # afficher la liste


print()
print("*" * 7 + " END " + "*" * 7)
print()

print("Ex3:")


# J'ai declaré et initialisé les listes de 3ème question
distances = [44, 67, 94, 32, 75]
tempsCourreurA = [147, 283, 376, 105, 302]
tempsCourreurB = [129, 290, 356, 122, 298]

# Je demande un numéro de trajet à l'utilisateur, et j'affiche la distance et
# les temps des coureurs A et B pour ce trajet.

x = -1

while (x < 0 or x > 4):
    x = int(input("Rentrez un nombre: "))

print(f"""
    trajet: {x}
    Distance: {distances[x]}
    temps CourreurA: {tempsCourreurA[x]}
    temps CourreurB: {tempsCourreurB[x]}      
""")

print()
print("*" * 7 + " END " + "*" * 7)
print()

print("Ex4:")
joursOuvres = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
weekEnd = ["samedi", "dimanche"]

semaine = list(joursOuvres + weekEnd)

while semaine[0] != "dimanche":
    semaine.append(semaine.pop(0))

for i in range(0, len(semaine)):
    print(f"Jour {i}: {semaine[i]}")

print()
print("*" * 7 + " END " + "*" * 7)
print()

print("Ex5:")
distances = [44, 67, 94, 32, 75]
tempsCourreurA = [147, 283, 376, 105, 302]
tempsCourreurB = [129, 290, 356, 122, 298]

distanceMin = 999
distanceMax = 0
for i in distances:
    if i < distanceMin:
        distanceMin = i

    if i > distanceMax:
        distanceMax = i

print(f" DistanceMin = {distanceMin}\n distanceMax = {distanceMax}")

print()
print("*" * 7 + " END " + "*" * 7)
print()

print("Ex6:")

semaine = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]

for i in range(0, len(semaine) - 1):
    semaine.insert(i, semaine.pop(len(semaine) - 1))
    print(semaine)

print()
print("*" * 7 + " END " + "*" * 7)
print()

print("Ex7:")
    
notes = list()

for i in range(0, 5):
    note = -1
    while(note < 0 or note > 20):
        note = int(input(f"note n°{i + 1}: "))
    notes.append(note)
somme = 0
for i in notes:
    somme = somme + i
moyenne = somme / 5
print(f"Moyenne des notes: {moyenne}")

