from time import sleep, perf_counter
from threading import Thread


def io_task(n):
    print("Task started...")
    sleep(n)
    print("Task finished!")


if __name__ == "__main__":
    start = perf_counter()

    threads = []

    for i in range(10):
        thread = Thread(target=io_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
