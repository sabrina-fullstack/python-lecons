def positive_values(numbers):
    result = []
    for number in numbers:
       if number > 0:
            result.append(number)
    return result

numbers = [3, 0, -2, 7]                  # ma liste de départ
result = positive_values(numbers)        # je filtre numbers : result = [3, 7]
print(result)                            # [3, 7]
print(numbers)                           # [3, 0, -2, 7], inchangée
print(positive_values([]))               # je filtre une AUTRE liste, vide : []