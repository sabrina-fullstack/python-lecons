def even_numbers(values):#nombres pairs
    result = []
    for value in values:
        if value % 2 == 0:#le reste de la division par 2 est 
            result.append(value)
    return result#nouvelle liste

print(even_numbers([3, 2, 4]))
print(even_numbers([]))