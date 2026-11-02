numbers = [8, 2, 5] # liste de nombres à trier
numbers.sort() # trie la liste en place
print(numbers) # affiche la liste triée
numbers = [8, 2, 5] # réinitialise la liste originale avant d'utiliser sorted()
ordered = sorted(numbers) # crée une nouvelle liste triée sans modifier la liste originale
print(ordered)  # affiche la liste triée sans modifier la liste originale
print(numbers) # affiche la liste originale, non modifiée par sorted()
numbers = [8, 2, 5] # réinitialise la liste originale avant d'utiliser sort()
result = numbers.sort() # trie la liste en place et retourne None
print(numbers)  # affiche la liste triée après l'appel à sort()
print(result) # affiche None car sort() trie la liste en place et ne retourne rien