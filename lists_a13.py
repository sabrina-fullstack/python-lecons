numbers = [4, 7, 4, 2, 4]   # liste de nombres dans laquelle chercher
search_text = input("Search for: ") # demande à l'utilisateur de saisir le nombre à rechercher
search = int(search_text) # convertit le texte saisi en entier
positions = [] # liste pour stocker les positions où le nombre recherché apparaît

for i in range(len(numbers)): # parcourt la liste avec les indices
    if numbers[i] == search: # si le nombre correspond à la recherche
        positions.append(i) # ajoute l'indice à la liste des positions
print(positions) # affiche la liste des positions mises à jour
