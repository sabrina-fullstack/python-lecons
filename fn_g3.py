x = 10

def f():
    x = 5
    print("dans f :", x)

f()
print("dehors :", x)

def g():
    global x
    x = 99

g()
print("apres g :", x)