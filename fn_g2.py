def total(*args):
    print(args)
    return sum(args)

def show(**kwargs):
    print(kwargs)

print(total(1, 2, 3))
print(total())
show(name="Dana", age=25)