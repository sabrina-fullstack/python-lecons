numbers = {10, 20, 30}
numbers.discard(20)
numbers.discard(99)
if 30 in numbers:                      # à toi : 30 est dans numbers
    numbers.remove(30)
if 99 in numbers:                      # à toi : 99 est dans numbers
    numbers.remove(99)
print(sorted(numbers))