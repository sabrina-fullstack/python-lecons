def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1                  
        else:
            counts[word] = 1                                 
    return counts

print(count_words(["apple", "pear", "apple"]))
print(count_words([]))
print(count_words(["a", "a", "a"]))