count_text = input("How many names? ") # poser la question dans un input 
count = int(count_text) # transformer le string en int
participants = [] # créer une liste

for participant in range(1, count + 1): # boucle
    name = input("Enter a name: ")# poser la question entrer le nom 
    if name not in participants:#  si le nom n'est pas dans la liste
        participants.append(name) # ajouter le nom

cancel = input("Cancel registration for: ")# poser la question entrer le nom a annuler 
if cancel in participants:# si le nom est dans la liste
    participants.remove(cancel)# retirer le nom


print("Registration order:", participants) # afficher la liste
print("Sorted:", sorted(participants)) # afficher la liste triée
print("Count:", len(participants)) # afficher le nombre de participants


