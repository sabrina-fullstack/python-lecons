def get_element(lst, index):
    if len(lst) == 0:
        raise ValueError("List is empty")                       # à toi : raise ValueError("List is empty")
    if index < 0:
        raise IndexError("Index cannot be negative")                        # à toi : raise IndexError("Index cannot be negative")
    return lst[index]

try:
    print("Element:", get_element([5, 6, 7], -1))
except IndexError as e:
    print("Index problem:", e)
except ValueError as e:
    print("Value problem:", e)
except Exception as e:
    print("Other problem:", e)
finally:
    print("Access attempt finished")