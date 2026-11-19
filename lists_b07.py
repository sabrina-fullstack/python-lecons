def average_scores(scores):
    if len(scores) == 0:
        return None
    total = 0
    for score in scores:
        total = total + score
    return total / len(scores)

print(average_scores([60, 70, 80]))
print(average_scores([]))