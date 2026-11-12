def add_item(item, box=[]):
    box.append(item)
    return box

print(add_item("a"))
print(add_item("b"))

def add_item_ok(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box

print(add_item_ok("a"))
print(add_item_ok("b"))