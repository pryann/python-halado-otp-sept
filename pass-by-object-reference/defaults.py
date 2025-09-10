def add_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print(add_to_basket("apple"))
print(add_to_basket("orange"))
print(add_to_basket("banana"))
