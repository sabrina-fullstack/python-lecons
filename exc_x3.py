def f():
    print("A")
    raise Exception("Boom")
    print("B")  

try:
    f()
except Exception:
    print("C")
finally:                                       
     print("D")
print("E")