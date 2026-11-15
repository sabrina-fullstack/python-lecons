class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

u1 = User("Dana", "dana@mail.com")
u2 = User("Avi", "avi@mail.com")
print(u1.name, u1.email)
print(u2.name, u2.email)