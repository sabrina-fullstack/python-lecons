values = {2, 4} # set {2, 4}
values.add(2) # 2 est déjà là, donc {2, 4}
values.update([4, 6, 6]) # 4 déjà là, 6 une seule fois, donc {2, 4, 6}
result = values.add(8) #{2, 4, 6, 8}
print(sorted(values))
print(result)