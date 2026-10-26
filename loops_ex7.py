passed_count = 0

for student in range(1, 5):
    score_text = input("Enter a score: ")
    score = int(score_text)

    if score>=60:
        passed_count = passed_count+1

print("Passed count:", passed_count)