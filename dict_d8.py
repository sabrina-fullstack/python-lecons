def add_stock(stock, product, quantity):
    if product in stock:                
        stock[product] += quantity                        
    else:
        stock[product] = quantity
                                    

stock = {"pen": 2}
result = add_stock(stock, "pen", 3)
add_stock(stock, "book", 4)
print(stock)
print(result)
empty_stock = {}
add_stock(empty_stock, "pen", 0)
print(empty_stock)