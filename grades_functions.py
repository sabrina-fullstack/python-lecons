def is_passing(score):
    return score >= 60


def show_report(total_score, passed):
    print("Total:", total_score)
    print("Passed count:", passed)


count_text = input("How many students? ")
count = int(count_text)
total = 0
passed_count = 0

for student in range(1, count + 1):
    print("Student", student)
    score_text = input("Enter a score: ")
    score = int(score_text)
    total = total + score   
    if is_passing(score):
        passed_count = passed_count + 1

show_report(total, passed_count)