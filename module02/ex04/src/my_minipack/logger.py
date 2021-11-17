import time
from random import randint
import os


def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        username = os.environ.get('USER')
        elapsed_time_str = f"{elapsed_time:.3f} s"
        if elapsed_time_str == "0.000 s":
            elapsed_time_str = f"{elapsed_time*1000:.3f} ms"
        with open('machine.log', 'a') as f:
            f.write(f"({username})Running: {func.__name__}\t"
                    + f"[ exec-time = {elapsed_time_str} ]\n")
        return result
    return wrapper
