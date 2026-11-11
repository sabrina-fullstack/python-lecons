def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")                        # à toi : lancer ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)                              # à toi : la somme divisée par le nombre d'éléments

try:
    print("Average:", calculate_average([10, 20, 30]))
    print("Average:", calculate_average([]))
except ValueError as e:
    print("Error:", e)
finally:
    print("Calculation finished")