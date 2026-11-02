original = [2, 4]
same = original #la même liste avec deux noms differents
copied = original.copy()# crée une nouvelle liste avec les mêmes éléments que l’original.
same.append(6)#on écrit 6 dans le cahier de same
copied[0] = 99#on modifie le premier élément de copied, sans affecter original ni same
print(original)
print(same)
print(copied)