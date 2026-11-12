nums = [1, 2, 3, 4]
labels = ["even" if x % 2 == 0 else "odd" for x in nums]
print(labels)

name = ""
display_name = name if name else "Guest"
print(display_name)
name = "Dana"
print(name if name else "Guest")