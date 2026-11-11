import copy

original = [[1, 2], [3, 4]]
same = original
same[0].append(100)
print(original)

original = [[1, 2], [3, 4]]
sliced =original[:]
sliced[0].append(200)
print(original)

original = [[1, 2], [3, 4]]
deep =copy.deepcopy(original)
deep[0].append(300)
print(original)