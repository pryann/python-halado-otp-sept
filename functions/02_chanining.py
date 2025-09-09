def add_cheese(burger):
    burger["cheese"] = True
    return burger


def add_double_meal(burger):
    burger["double_meal"] = True
    return burger


def add_glunten_free_bun(burger):
    burger["gluten_free_bun"] = True
    return burger


def remove_onion(burger):
    burger["onion"] = False
    return burger


def make_burger(basic_burger, *funcs):
    burger = basic_burger
    for func in funcs:
        burger = func(burger)
    return burger


custom_burger_1 = make_burger(
    {}, add_cheese, add_double_meal, add_glunten_free_bun, remove_onion
)

custom_burger_2 = make_burger({}, add_cheese, remove_onion)
print(custom_burger_1)
print(custom_burger_2)
