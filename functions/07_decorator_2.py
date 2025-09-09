def basic_decorator(fn):
    def wrapper(name):
        print("Before function call")
        fn(name)
        print("After function call")

    return wrapper


@basic_decorator
def say_hello(name):
    print(f"Hello {name}!")


say_hello("Ruff")

# result = basic_decorator(say_hello)
# result()

# basic_decorator(say_hello)()  # same as above
