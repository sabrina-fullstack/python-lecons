count_text = input("How many students? ")
count = int(count_text)
total=0
passed_count = 0
for student in range(1,count+1):
    print("Student", student)
    score_text = input("Enter a score: ")
    score = int(score_text)
    total = total + score
    if score >= 60:
        passed_count = passed_count + 1
print("Total:", total)
print("Passed count:", passed_count)

if count > 0:
    print("Average:", total/count)
