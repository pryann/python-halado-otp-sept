from time import perf_counter


def runtime_benchmark(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print(f"Function {fn.__name__} took {end - start:.6f} seconds to execute")
        return result

    return wrapper


@runtime_benchmark
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


factorial(10)
factorial(100_000)
