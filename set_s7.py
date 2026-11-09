def common_students(first, second):
    return first.intersection(second)           # à toi : l'intersection de first et second

group_a = {"Dan", "Noa"}
group_b = {"Noa", "Maya"}
print(sorted(common_students(group_a, group_b)))
print(sorted(group_a))
print(sorted(group_b))
print(sorted(common_students(group_a, set())))