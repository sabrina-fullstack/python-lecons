numbers = [7] # liste d'entiers
if len(numbers) == 0: # verifie si la liste est vide et si c'est le cas affiche ....
    print ("No numbers") # affiche "No numbers"
else: # sinon
    largest = numbers[0]# le plus grand est le premier
    for number in numbers:# pour chaque entier dans le tableau
        if number > largest:# si le plus grand est plus petit que l'entier
            largest = number# le plus grand devient l'entier
    print("Largest:", largest)# affiche le plus grand