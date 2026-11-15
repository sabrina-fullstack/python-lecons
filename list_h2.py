nums = [1, 2, 3, 4, 5, 6]
print({x % 3 for x in nums})
print({x: x * x for x in nums})
words = ["a", "bb", "ccc"]
print({w: len(w) for w in words})