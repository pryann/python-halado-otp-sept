def increase_by_one(x):
    return x + 1


# increase_by_one_lambda = lambda x: x + 1


def apply(numbers, func):
    # result = []
    # for number in numbers:
    #     result.append(func(number))
    # return result
    return [func(number) for number in numbers]


numbers = [1, 2, 3, 4, 5]
print(apply(numbers, lambda x: x**3))

print(apply(numbers, increase_by_one))

numbers_2 = [10, 20, 30, 40, 50, 53, 51]
# comprehension
even_numbers = [n for n in numbers_2 if n % 2 == 0]
print(even_numbers)
