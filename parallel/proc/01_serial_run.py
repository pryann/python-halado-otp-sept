from time import sleep, perf_counter


def process_fn():
    sleep(2)

if __name__ == "__main__":
    start = perf_counter()
    process_fn()
    process_fn()
    process_fn()
    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")