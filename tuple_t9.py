def total_and_count(values):
    total = 0
    count = 0
    for value in values:
        total = total + value         # à toi : ajouter la valeur
        count = count + 1       # à toi : ajouter 1
    return (total, count,)          # à toi : renvoyer total et count

values = (4, 7, 4)
total, count = total_and_count(values)
print("Total:", total)
print("Count:", count)
print(total_and_count(()))