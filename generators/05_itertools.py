from itertools import count, repeat

# endless interátor
# def count(start=0, step=3):
#     n = start
#     while True:
#         yield n
#         n += step


# counter = count()
# print(list(next(counter) for _ in range(5)))

counter = count(0, 3)
print(list(next(counter) for _ in range(5)))


# def repeat(object, times=None):
#     if times is None:
#         while True:
#             yield object
#     else:
#         for i in range(times):
#             yield object


# repeater = repeat("text", 5)
# print(list(next(repeater) for _ in range(5)))

repeater = repeat("text", 5)
print(list(next(repeater) for _ in range(5)))


def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


# range (0,1,2,3,4,5,6,7,8,9)
# lambda 0 : 0 % 2 = 0  -> yield 0
# lambda 1 : 1 % 2 = 1  -> not yield 1
# lambda 2 : 2 % 2 = 0  -> yield 2
# lambda 3 : 3 % 2 = 1  -> not yield 3
# lambda 4 : 4 % 2 = 0  -> yield 4
# lambda 5 : 5 % 2 = 1  -> not yield 5
# lambda 6 : 6 % 2 = 0  -> yield 6
# lambda 7 : 7 % 2 = 1  -> not yield 7
# lambda 8 : 8 % 2 = 0  -> yield 8
# lambda 9 : 9 % 2 = 1  -> not yield 9


iterator_filteralse = filterfalse(lambda x: x % 2, range(10))
print([i for i in iterator_filteralse])

# iterator_filteralse = filterfalse(lambda x: x % 2, range(10))
# print([i for i in iterator_filteralse])
# print(bool(0))
# print(bool(1))
# print(bool(-1))
