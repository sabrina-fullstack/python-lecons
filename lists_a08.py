count = int(input("How many numbers? "))
numbers = []

for number in range(count):
    number_text = input("Enter a number: ")
    numbers.append(int(number_text))

print(numbers)
print("Count:", len(numbers))