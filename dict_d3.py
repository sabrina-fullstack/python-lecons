stock = {"pen": 0, "book": 4}
if "pen" in stock:
    print(stock["pen"])
else:
    print("Missing")
print(stock.get("eraser", 0))
print("eraser" in stock)