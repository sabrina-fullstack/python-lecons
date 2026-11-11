def set_age(age):
  assert age >= 0, "Age cannot be negative"                         # à toi : assert age >= 0, "Age cannot be negative"
  print("Age set to", age)

set_age(5)
try:
    set_age(-1)
except AssertionError as e:
    print("Error:", e)