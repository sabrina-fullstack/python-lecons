def has_requirements(required, learned):
    return required.issubset(learned)               # à toi : required est-il un sous-ensemble de learned ?

need = {"Python", "SQL"}
print(has_requirements(need, {"Python", "SQL", "HTML"}))
print(has_requirements(need, {"Python"}))
print(has_requirements(set(), {"Python"}))