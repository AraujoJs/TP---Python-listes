# -*- coding: utf-8 -*-
"""
TP NSI 1ére Générale 2022-2023
José ARAUJO

Liste et boucles for
"""
joursOuvres = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
weekEnd = ["samedi", "dimanche"]

semaine = list(joursOuvres + weekEnd)

while semaine[0] != "dimanche":
    semaine.append(semaine.pop(0))

for i in range(0, len(semaine)):
    print(f"Jour {i}: {semaine[i]}")
    
    