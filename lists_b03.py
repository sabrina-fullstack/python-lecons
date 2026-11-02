def count_passing(scores):#scores is a list
    passed = 0 #variable
    for score in scores: #score is a variable
        if score >= 60: # if score is greater than or equal to 60
            passed = passed + 1 #passed is equal to passed + 1
          
    return passed #return passed
print(count_passing([59, 60, 100])) #59, 60, 100
print(count_passing([])) #empty
print(count_passing([59, 59]))

