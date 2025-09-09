abc = "abc"
print(abc[0])

# TypeError: 'str' object does not support item assignment
# abc[0] = "x"

a, b, c = abc
print(a, b, c)

name = "Gergely"
first, second, *other = name
print(first, second, other)

names = ["Anna", "Béla", "Cecil", "Dénes", "Eszter"]
first_item, *_, last_item = names
print(first_item, last_item)

squares = (i**2 for i in range(1, 11))
i, j, k, *_ = squares
print(i, j, k)
