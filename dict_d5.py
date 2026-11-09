prices = {"pen": 5, "book": 20, "eraser": 3}
total = 0
for name, price in prices.items():          # à toi : parcourir les paires de prices
    print(name, price)
    total = total + price
print("Total:", total)
print(list(prices.keys()))
print(list(prices.values()))