def passing_scores(scores):
    result = {}
    for name in scores:
        if scores[name] >= 60:
            result[name] = scores[name]
    return result

grades = {"Noa": 80, "Dan": 40, "Maya": 60}
print(passing_scores(grades))
print(grades)
print(passing_scores({}))