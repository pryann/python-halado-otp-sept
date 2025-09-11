from time import sleep, perf_counter
from multiprocessing import Process


def process_fn():
    sleep(2)


if __name__ == "__main__":
    start = perf_counter()
    process_1 = Process(target=process_fn)
    process_2 = Process(target=process_fn)
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()

    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
