def add_bonus(scores, bonus):
    for i in range(len(scores)):
        new_score = scores[i] + bonus
        if new_score > 100:
            new_score = 100
        scores[i] = new_score

scores = [55, 90, 100]
add_bonus(scores, 10)
print(scores)

empty_scores = []
add_bonus(empty_scores, 10)
print(empty_scores) 