# -*- coding: utf-8 -*-
"""
TP NSI 1ére Générale 2022-2023
José ARAUJO
Créez 2 listes
"""

joursOuvres = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
weekEnd = ["samedi", "dimanche"]

semaine = list(joursOuvres + weekEnd)

"""
Question 2:
Utiliser "pop" et "insert" pour modifier la liste semaine
afin que la semaine commence le dimanche
"""

# semaine.insert(0, semaine.pop(6))

while semaine[0] != "dimanche":
    semaine.append(semaine.pop(0))

print(semaine) # afficher la liste

