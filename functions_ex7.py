def ticket_price(age):
    if age <= 5:
        return 0
    if age >= 6 and age < 18:
        return 20
    if age >= 18:
        return 40
   


age_text = input("Enter age: ")
age = int(age_text)
price = ticket_price(age)
print("Ticket price:", price)
