def log_error(message):
    print(f"ERROR: {message}")


log_error_fn = log_error
log_error_fn("Something went wrong!")


# higher order function
def outer_fn(text):
    message = text.upper()

    def inner_fn():
        print(message)

    inner_fn()


outer_fn("hello")


# closure
def make_incrementor(n):
    def incrementor(x):
        return x + n

    return incrementor


make_incrementor_result = make_incrementor(10)
print(make_incrementor_result(5))  # 15

print(make_incrementor(20)(5))  # 25