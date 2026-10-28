colors = ["red", "blue", "red", "green"] # liste initiale des couleurs
colors.remove("red") # retire la première occurrence de "red"
removed = colors.pop() # retire le dernier élément et le renvoie green
print("Removed:", removed) # affiche l'élément retiré green
print(colors)              # ['blue', 'red'] # affiche la liste après suppression