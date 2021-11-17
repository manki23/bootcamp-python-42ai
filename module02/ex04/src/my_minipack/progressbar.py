import time


def progressbar(lst):
    index = 1
    begin_time = time.time()
    for elem in lst:
        p = int((index / len(lst)) * 100)
        elapsed_time = time.time() - begin_time
        eta = (elapsed_time / index) * len(lst)
        str_p = "=" * int(p / 5) + ">" + " " * (20 - int(p / 5))
        print(f"\rETA: {eta:.2f}s [{p: 3d}%][{str_p}] {index}/{len(lst)} \
            | elapsed time {elapsed_time:.2f}s", end="")
        index += 1
        yield elem
