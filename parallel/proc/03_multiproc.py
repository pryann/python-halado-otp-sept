from time import sleep, perf_counter
from multiprocessing import Process


def process_fn():
    sleep(2)


def main():
    processes = []
    for _ in range(16):
        p = Process(target=process_fn)
        processes.append(p)
        p.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
