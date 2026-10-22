name = input("Enter your name: ")
price = 0
age_text = input("Enter your age: ")
age = int(age_text)

if age < 6:
    price = 0
elif age < 18:
    price = 20
else:
    price = 40

print("Hello", name)
print("Ticket price:", price, "NIS")