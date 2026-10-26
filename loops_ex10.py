number_text = input("Enter a number: ")
number = int(number_text)
for factor in range(1, 11):
    
    print(number, "x", factor, "=", number * factor)