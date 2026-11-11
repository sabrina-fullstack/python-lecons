def withdraw(amount):
    if amount <= 0:
        raise ValueError("Invalid amount")                        # à toi : lancer une ValueError avec le message
    print("Withdrawn:", amount)

try:
    withdraw(-5)
except ValueError as e:                          # à toi : attraper ValueError et le nommer e
    print("Error:", e)
finally:                                        # à toi : le bloc qui s'exécute toujours
    print("Operation finished")