first_text = input("Enter the first number: ")
first_number = int(first_text)
second_text = input("Enter the second number: ")
second_number = int(second_text)

if first_number > second_number:
    print("First is larger")
elif first_number < second_number:
    print("Second is larger")
else:
    print("Equal")
