from threading import Thread
from time import sleep, ctime
from concurrent.futures import ThreadPoolExecutor


def log_service(thread_name, delay):
    while logging:
        sleep(delay)
        print(f"{thread_name}: {ctime()}")


if __name__ == "__main__":
    max_tasks = 5
    logging = True

    with ThreadPoolExecutor(max_workers=max_tasks) as executor:
        args = ((f"Thread-{i}", i + 1) for i in range(max_tasks))
        # print(*args)
        # print(*zip(*args))
        executor.map(log_service, *zip(*args))
        sleep(10)
        logging = False
