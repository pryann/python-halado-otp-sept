def apply_vat(tax_rate_in_percent):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * (1 + tax_rate_in_percent / 100)

        return wrapper

    return decorator


def apply_discount(discount_in_percent):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * (1 - discount_in_percent / 100)

        return wrapper

    return decorator


@apply_vat(27)
@apply_discount(10)
def summa(a, b):
    return a + b


print("Return value", summa(10, 20))


products = [
    {"id": 1, "name": "Product 1", "price": 1000, "count": 2},
    {"id": 2, "name": "Product 2", "price": 2000, "count": 0},
    {"id": 3, "name": "Product 3", "price": 3000, "count": 4},
]

# validálja, hogy mind a 4 tulajdonság megvan e ,
# és az id, az ár és a count pozitív szám, a name string és nem üres
# ha hiba van kiírja melyik id-jú termékkel van a gond, és mi a hiba


def product_validator():
    pass


@apply_vat(27)
def total_price(products):
    # summa = 0
    # for i in products:
    #     summa += i["price"] * i["count"]
    # return summa

    return sum(p["price"] * p["count"] for p in products)


print("Total price with VAT:", total_price(products))
