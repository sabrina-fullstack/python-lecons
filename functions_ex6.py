def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


n_text = input("Enter n: ")
n = int(n_text)
print("Total:", sum_to(n))