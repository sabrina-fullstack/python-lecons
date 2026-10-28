def sum_to(n):
    total = 0
    for number in range(1, n + 1):
        total = total + number
    return total
print(sum_to(3))
print(sum_to(0))