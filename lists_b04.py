def contains_value(values, target):
 for value in values:
  if value == target:
    return True
 return False
print(contains_value([4, 8, 4], 8))
print(contains_value([4, 8, 4], 7))
print(contains_value([], 8))