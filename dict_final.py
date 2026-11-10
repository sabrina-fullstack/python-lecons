def summarize_sales(sales):
    totals = {}
    buyers = set()
    for name, product, quantity in sales:
        if product not in totals:
            totals[product] = 0
        totals[product] += quantity
        buyers.add(name)
    return totals, buyers

sales = [
    ("Noa", "pen", 2),
    ("Dan", "book", 1),
    ("Noa", "pen", 3),
    ("Maya", "book", 2)
]
totals, buyers = summarize_sales(sales)
print("Buyers:", sorted(buyers))
print("Products:", len(totals))
for product in sorted(totals):
    print(product, totals[product])
empty_totals, empty_buyers = summarize_sales([])
print(empty_totals)
print(sorted(empty_buyers))