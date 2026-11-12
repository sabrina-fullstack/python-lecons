name = "Dana"
age = 25
phone = "0501234567"
print(f"Bonjour {name}, tu as {age} ans")
print(f"L'an prochain : {age + 1} ans")
if phone.isdigit() and phone.startswith("05"):
    print("Numéro valide")
else:
    print("Numéro invalide")