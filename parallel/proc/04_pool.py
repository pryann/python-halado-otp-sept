from time import sleep, perf_counter
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, as_completed


def process_fn(sec):
    sleep(sec)
    return f"Slept for {sec} seconds"


def main():
    with ProcessPoolExecutor() as executor:
        results = [executor.submit(process_fn, i) for i in range(1, 6)]
        for completed in as_completed(results):
            print(completed.result())


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
