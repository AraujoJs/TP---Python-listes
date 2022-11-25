# -*- coding: utf-8 -*-
"""
TP NSI 1ére Générale 2022-2023
José ARAUJO

Liste et boucles for
"""
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
