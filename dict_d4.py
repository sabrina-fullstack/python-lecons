contacts = {"Noa": "111", "Dan": "222", "Maya": "333"}
if "Dan" in contacts:                              # à toi : "Dan" est dans contacts
    removed = contacts.pop("Dan")
    print(removed)
if "Noa" in contacts:                              # à toi : "Noa" est dans contacts
    del contacts["Noa"]
if "Omer" in contacts:                              # à toi : "Omer" est dans contacts
    del contacts["Omer"]
print(contacts)