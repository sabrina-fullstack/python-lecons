def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Dana"))
print(greet("Dana", "Shalom"))
print(greet(greeting="Hi", name="Avi"))