import gzip

with gzip.open("data.txt.gz", "wt") as f:        # à toi : écriture en texte
    f.write("Compressed text")

with gzip.open("data.txt.gz", "rt") as f:        # à toi : lecture en texte
    print(f.read())