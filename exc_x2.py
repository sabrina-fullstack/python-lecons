def parse_number(value):
    if value == "":
        raise ValueError("Empty string")                      # à toi : raise ValueError("Empty string")
    return int(value)

for text in ["12", "", "abc"]:
    try:
        number = parse_number(text)
        print("Number:", number)
    except ValueError as e:                      # à toi : le type d'erreur à attraper
        print("Error:", e)         # à toi : afficher la variable e