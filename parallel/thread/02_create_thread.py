from time import sleep, perf_counter
from threading import Thread


def io_task():
    print("Task started...")
    sleep(2)
    print("Task finished!")


if __name__ == "__main__":
    start = perf_counter()

    thread_1 = Thread(target=io_task)
    thread_2 = Thread(target=io_task)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
