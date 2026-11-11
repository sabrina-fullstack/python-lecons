with open("data.txt", "r") as source:
    data = source.read()
with open("copy.txt", "w") as target:           # à toi : le mode écriture
    target.write(data)                              # à toi : écrire data
with open("copy.txt", "r") as f:
    print(f.read())