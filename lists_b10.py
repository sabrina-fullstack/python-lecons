def append_one(values):#ajoute un
    values.append(99)

def replace_values(values):#remplace les valeurs
    values = [0]

numbers = [2, 4]
append_one(numbers) #la liste du programme
replace_values(numbers)
print(numbers)

empty_numbers = []
append_one(empty_numbers)
replace_values(empty_numbers)
print(empty_numbers)