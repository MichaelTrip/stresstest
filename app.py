# app.py

import time
import multiprocessing

def worker_cpu():
    # worker function, runs in an infinite loop to use CPU cycles
    while True:
        x = 20 * 20

def worker_memory():
    # worker function, consumes a significant amount of memory
    huge_element = bytearray(1024 * 1024 * 500)  # Consume 500MB of Memory
    while True:
        time.sleep(10)

if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker_cpu)
        jobs.append(p)
        p.start()

        p = multiprocessing.Process(target=worker_memory)
        jobs.append(p)
        p.start()
