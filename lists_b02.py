def total_values(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
print(total_values([3, -1, 5]))
print(total_values([]))
x = total_values([3, -1, 5])
print(x)