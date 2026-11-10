def sell_item(stock, product, quantity):
    if quantity <= 0:
        return False                         # à toi : return False
    if product not in stock:
        return False                         # à toi : return False
    if stock[product] < quantity:
        return False
    stock[product] -= quantity
    return True

stock = {"pen": 5, "book": 2, "eraser": 0}
print(sell_item(stock, "pen", 3))
print(sell_item(stock, "book", 4))
print(sell_item(stock, "eraser", 1))
print(sell_item(stock, "marker", 1))
print(sell_item(stock, "pen", 0))
print(sell_item({}, "pen", 1))
for product, quantity in stock.items():
    print(product, quantity)
print(sell_item(stock, "pen", 2))
print(stock["pen"])