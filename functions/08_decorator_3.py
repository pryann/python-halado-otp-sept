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
    {
        "id": 1,
        "name": "Product 1",
        "price": "1000",
    },
    {"id": 2, "name": "Product 2", "price": 2000, "count": 0},
    {"id": 3, "name": "Product 3", "price": 3000, "count": 4},
    {"id": 4, "name": "", "price": -100, "count": -2},
]

# validálja, hogy mind a 4 tulajdonság megvan e ,
# és az id, az ár és a count pozitív szám, a name string és nem üres
# ha hiba van kiírja melyik id-jú termékkel van a gond, és mi a hiba


def product_validator(fn):
    def wrapper(products, *args, **kwargs):
        valid_products = []
        for product in products:
            errors = []

            required_keys = ["id", "name", "price", "count"]
            for key in required_keys:
                if key not in product:
                    errors.append(f"Missing key: '{key}'")

            if "id" in product:
                if not isinstance(product["id"], int) or product["id"] <= 0:
                    errors.append("'id' must be a positive integer")

            if "price" in product:
                if (
                    not isinstance(product["price"], (int, float))
                    or product["price"] <= 0
                ):
                    errors.append("'price' must be a positive number")

            if "count" in product:
                if not isinstance(product["count"], int) or product["count"] < 0:
                    errors.append("'count' must be a non-negative integer")

            if "name" in product:
                if not isinstance(product["name"], str) or not product["name"].strip():
                    errors.append("'name' must be a non-empty string")

            if errors:
                print(
                    f"Error with product 'id' {product.get('id', '?')}: {' | '.join(errors)}"
                )
            else:
                valid_products.append(product)

        return fn(valid_products, *args, **kwargs)

    return wrapper


@product_validator
@apply_vat(27)
def total_price(products):
    return sum(p["price"] * p["count"] for p in products)


print("Total price with VAT:", total_price(products))
