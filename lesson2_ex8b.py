score_text = input("Enter your score: ")
score = int(score_text)

if score < 0 or score > 100:
    print("Invalid score")
else:
    print("Valid score")