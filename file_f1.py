with open("data.txt", "r") as f:       # à toi : le mode lecture
    lines = f.readlines()
print("Number of lines:", len(lines))           # à toi : le nombre d'éléments de lines