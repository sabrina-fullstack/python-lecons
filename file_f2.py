name = input("Name: ")
age = input("Age: ")
with open("user.txt", "w") as f:                # à toi : le mode écriture
    f.write("Name: " + name + "\n")
    f.write("Age: " + age + "\n")                                   # à toi : "Age: " + age + "\n"
with open("user.txt", "r") as f:
    print(f.read())                                     # à toi : lire tout le fichier