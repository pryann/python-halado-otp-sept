from time import sleep, perf_counter
from threading import current_thread

thread = current_thread()

print("Current thread:", thread.name)


def io_task():
    print("Task started...")
    sleep(2)
    print("Task finished!")


if __name__ == "__main__":
    start = perf_counter()
    io_task()
    io_task()
    io_task()
    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
