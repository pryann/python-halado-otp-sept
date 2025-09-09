def simple_generator():
    yield 1
    yield 2
    yield 3


ids = simple_generator()
print(next(ids))
print(next(ids))
print(next(ids))

for i in simple_generator():
    print(i)


id_gens = (num for num in range(1, 10))
print(next(id_gens))
print(next(id_gens))

print(sum(num for num in range(1, 1000001)))


def square_input(start=1):
    while True:
        yield start
        start += 1


squares = square_input(5)
print(next(squares))
print(next(squares))
print(next(squares))


def square_input_send():
    while True:
        value = yield
        yield value**2


squares_send = square_input_send()
next(squares_send)
print(squares_send.send(5))
next(squares_send)
print(squares_send.send(25))
