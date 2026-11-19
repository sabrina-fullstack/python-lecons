def count_occurrences(values, target):
    counter = 0
    for value in values:
        if value == target:
            counter = counter + 1
    return counter

print(count_occurrences([4, 8, 4], 4))
print(count_occurrences([4, 8, 4], 7))
print(count_occurrences([], 4))