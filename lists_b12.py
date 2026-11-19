def count_passing(scores):
    passed = 0
    for score in scores:
        if score >= 60:
            passed = passed + 1
    return passed

def average_scores(scores):
    if len(scores) == 0:
        return None
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

def show_report(scores):
    if len(scores) == 0:
        print("No scores")
    else:
        print("Count:", len(scores))
        print("Passed:", count_passing(scores))
        print("Average:", average_scores(scores))

count = int(input("How many students? "))
scores = []
for index in range(count):
    score = int(input("Enter a score: "))
    scores.append(score)
show_report(scores)
