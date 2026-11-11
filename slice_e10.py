def reverse_list(values):
    return values[::-1]                    # à toi : values à l'envers, avec un slice

numbers = [1, 2, 3, 4]
result = reverse_list(numbers)
print(result)
print(numbers)
print(reverse_list([]))