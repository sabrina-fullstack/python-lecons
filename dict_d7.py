def get_quantity(stock, product):
    if product in stock:
      return stock[product]
    else:
      return 0  
stock = {"pen": 0, "book": 4}
print(get_quantity(stock, "book"))
print(get_quantity(stock, "pen"))
print(get_quantity(stock, "eraser"))
print(get_quantity({}, "book"))
print(stock)