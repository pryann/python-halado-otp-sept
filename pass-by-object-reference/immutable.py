a = 100
a = 110

# 000a - 100 X
# 000b - 110

a_copy = a
a_copy_2 = a_copy

# a ----> 000b - 110
# a_copy --^
# a_copy_2 --^

a_copy = 120
# a_copy ----> 000c - 120

# a ----> 000b - 110
# a_copy_2 --^
print(a, a_copy, a_copy_2)


def log_value(x):
    x = x + 1
    print("inside function value", x)
    print("inside function id", id(x))


value = 10
print("Original global varaible value and id", value, id(value))
log_value(value)
print("global variable value and id after function call", value, id(value))


def local():
    global value
    value = 100
    print(value)


local()
print(value)
