yearly_salaries = [20_000, 35_000, 44_000]
print("yearly_salaries id", id(yearly_salaries))

yearly_salaries_copy = yearly_salaries
print("yearly_salaries_copy id", id(yearly_salaries_copy))

yearly_salaries.append(50_000)
print(yearly_salaries)
print(yearly_salaries_copy)

# yearly_salaries  ->  000a - [20_000, 35_000, 44_000]
# yearly_salaries_copy -^

yearly_salaries_copy.append(60_000)
print(yearly_salaries)
print(yearly_salaries_copy)

yearly_salaries_copy = [100_000, 200_000]
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

prices = [10_000, 20_000, 30_000]


def apply_vat(list_of_prices, vat_in_percent):
    copy = list_of_prices.copy()
    # copy = list_of_prices[:]
    for i in range(len(copy)):
        copy[i] * (1 + vat_in_percent / 100)
    return copy

    # increased_price = []
    # for i in range(len(list_of_prices)):
    #     increased_price.append(list_of_prices[i] * (1 + vat_in_percent / 100))
    # return increased_price
    # return list(map(lambda price: price * (1 + vat_in_percent / 100), list_of_prices))
    return [price * (1 + vat_in_percent / 100) for price in list_of_prices]


print(apply_vat(prices, 27))
print(prices)

# not too nice
# def apply_vat(vat_in_percent):
#     return [price * (1 + vat_in_percent / 100) for price in prices]


def change_list(list_1, list_2):
    return [x * 2 for x in list_1], [x * 3 for x in list_2]


# print(type(change_list([1, 2, 3], [4, 5, 6])))
# print(change_list([1, 2, 3], [4, 5, 6]))

changed_1, changed_2 = change_list([1, 2, 3], [4, 5, 6])
print(changed_1)
print(changed_2)
