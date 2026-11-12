full = "dana cohen"
print(full.upper ())
print(full.startswith("d"))
print(full[0:3])
print(full[::-1])
parts = full.split()
print(parts)
print(" ".join(parts))
print(f"Prénom : {parts[0]}, Nom : {parts[1]}, longueur : {len(full)} caractères")