def basic_decorator(fn):
    def wrapper():
        print("Before function call")
        fn()
        print("After function call")

    return wrapper


@basic_decorator
def say_hello():
    print("Hello!")


say_hello()

# result = basic_decorator(say_hello)
# result()

# basic_decorator(say_hello)()  # same as above
