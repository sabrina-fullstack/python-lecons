names = ["Noa", "Dan", "Noa"]
phones = ["111", "222", "333"]
contacts = {}
for i in range(len(names)):
  contacts[names[i]] = phones[i]             # à toi : contacts[clé] = valeur
print(contacts)
print(len(contacts))