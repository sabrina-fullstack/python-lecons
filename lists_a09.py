scores = [55, 80, 60, 45, 100]
total = 0
passed = 0

for score in scores:
    total = total + score
    if score >= 60:
        passed += 1

print("Total:", total)
print("Passed:", passed)