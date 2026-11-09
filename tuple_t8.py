def move_point(point, dx, dy):
    x, y = point             
    return (x + dx, y + dy)    

original = (2, 3) 
moved = move_point(original, 5, -1)
print(original)
print(moved)