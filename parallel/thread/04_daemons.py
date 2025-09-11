from threading import Thread
from time import sleep, ctime


def log_service(thread_name, delay):
    while True:
        sleep(delay)
        print(f"{thread_name}: {ctime()}")


if __name__ == "__main__":
    Thread(target=log_service, args=("Thread-1", 1.1), daemon=True).start()
    Thread(target=log_service, args=("Thread-2", 3), daemon=True).start()
    print("Other stuff")
    sleep(5)
    print("Main thread exit")
