def with_bonus(scores, bonus):
    new_scores = scores.copy()
    for i in range(len(new_scores)):
        new_score = new_scores[i] + bonus
        if new_score > 100:
            new_score = 100
        new_scores[i] = new_score
    return new_scores

scores = [55, 90, 100]
result = with_bonus(scores, 10)
print("Original:", scores)
print("With bonus:", result)