python = {"Avi", "Dan", "Noa"}
web = {"Dan", "Maya", "Noa"}
print(sorted(python.union(web)))
print(sorted(python.intersection(web)))
print(sorted(python.difference(web)))
print(sorted(python.symmetric_difference(web)))