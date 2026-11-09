scores = (50, 80, 60, 90)
total = 0
passed = 0
for score in scores:
    total = total + score   
    if score >= 60:        
        passed = passed + 1
print("Total:", total)
print("Passed:", passed)