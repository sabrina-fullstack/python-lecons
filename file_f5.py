import shelve

with shelve.open("storage.db") as db:
    db["user"] = {"name": "Bob", "age": 25}                            # à toi : {"name": "Bob", "age": 25}

with shelve.open("storage.db") as db:
    print(db["user"])                                # à toi : la clé "user"