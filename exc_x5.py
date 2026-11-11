def convert(value):
    try:
        return int(value)
    except ValueError:
        print("Logging error")
        raise                                       # à toi : relancer la même erreur (un seul mot)

try:
    convert("abc")
except ValueError as e:
    print("Caught outside:", e)