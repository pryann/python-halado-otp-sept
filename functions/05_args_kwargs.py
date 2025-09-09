def fn(a=0, b=0):
    print(a, b)


fn(10, 20)
fn(10)
fn()

# with open(file="example", mode="r", encoding="utf-8") as f:
#     content = f.read()
#     print(len(content))


# def calculate_price(price, tax_rate=27, discount=0):
#     return price * (1 + tax_rate / 100) - discount


def calculate_price(price, tax_rate, discount):
    return price * (1 + tax_rate / 100) - discount


calculate_price(1000, 27, 0)
calculate_price(
    discount=0,
    tax_rate=27,
    price=1000,
)


def log_args(a, b, *args):
    print(type(args), args)


log_args(10, 20)
log_args(10, 20, 30, 40, 50)


def log_kwargs(a, b, **kwargs):
    print(type(kwargs), kwargs)


log_kwargs(10, 20)
log_kwargs(10, 20, d=30, e=40, f=50)


def log_all(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)


log_all(10, 20, 30, d=40, e=50)


# only equality with strings and not empty filters
def generate_sql_filter(**filters):
    query = "SELECT * FROM product WHERE "
    for key, value in filters.items():
        query += f"{key}='{value}' AND "
    return query[:-5]  # remove last AND


generate_sql_filter(color="red", stock="yes", size="M")
