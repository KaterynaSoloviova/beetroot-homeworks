# Task 2
# Input data:
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total
# price of stock.

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

def total_price_in_stock(stock, prices):
    total_price = 0
    for key in stock:
        total_price += stock[key] * prices[key]
    return total_price

result = total_price_in_stock(stock, prices)
print(result)










