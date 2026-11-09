values = (5, 2, 5, 8, 5)
targets = (5, 9)
for target in targets:
    times = values.count(target)
    if target in values:                      
        position = values.index(target)          
    else:
        position = -1                      
    print(target, times, position)