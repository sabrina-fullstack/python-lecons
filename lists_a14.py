numbers = [] # liste de nombres à filtrer
non_negative = [] # liste pour stocker les nombres non négatifs
for number in numbers: # parcourt chaque nombre dans la liste
    if number >= 0: # si le nombre est non négatif
        non_negative.append(number) # ajoute le nombre à la liste des non-négatifs
print(non_negative) # affiche la liste des nombres non négatifs
print(numbers) # affiche la liste originale, non modifiée par le filtrage