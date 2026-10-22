score_text = input("Enter a number: ")
score = int(score_text)
print("You entered the number:", score)

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good") 
elif score >= 60:
    print("Passed")
else:
    print("Keep practicing")   