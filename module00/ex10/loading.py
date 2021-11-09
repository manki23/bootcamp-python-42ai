import time

def ft_progress(lst):
    index = 1
    begin_time = time.time()
    for elem in lst:
        progress = int((index / len(lst)) * 100)
        current_time = time.time()
        eta = ((current_time - begin_time) / index) * len(lst)
        str_progress = "=" * int(progress / 5) + ">" + " " * (20 - int(progress / 5))
        print(f"\rETA: {eta:.2f}s [{progress: 3d}%][{str_progress}] {index}/{len(lst)} | elapsed time {(current_time - begin_time):.2f}s", end="")
        index += 1
        yield elem

