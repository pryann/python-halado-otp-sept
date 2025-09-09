from functools import reduce

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
doubled_list = [i * 2 for i in numbers]
print(doubled_list)

doubled_list_fn = list(map(lambda i: i * 2, numbers))
print(doubled_list_fn)

even_list = [i for i in numbers if i % 2 == 0]

even_list_fn = filter(lambda i: i % 2 == 0, numbers)

sum_list = sum(numbers)

sum_list_fn = reduce(lambda acc, i: acc + i, numbers, 0)

# calculate gross prices, filter out above 500, sum them up
net_prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
standard_hungarian_tax_rate_in_percent = 27

result = reduce(
    lambda acc, i: acc + i,
    filter(
        lambda i: i < 500,
        map(
            lambda i: i * (1 + standard_hungarian_tax_rate_in_percent / 100), 
            net_prices
        ),
    ),
    0,
)

print(result)
