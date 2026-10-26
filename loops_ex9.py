word = input("Enter a word: ")
a_count = 0
for letter in word:
    if letter == "a":
        a_count = a_count + 1
print("A count:", a_count)