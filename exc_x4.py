def check(value):
    if value == "":
        raise ValueError("Empty string")
    if value == "x":
        raise Exception("Unknown problem")
    return value

for text in ["ok", "", "x"]:
    try:
        print("Result:", check(text))
    except ValueError as e:                      # à toi : l'erreur PRÉCISE d'abord (ValueError)
        print("Specific:", e)
    except Exception as e:                      # à toi : l'erreur GÉNÉRALE ensuite (Exception)
        print("General:", e)