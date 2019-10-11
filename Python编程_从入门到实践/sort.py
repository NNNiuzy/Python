from threading import Thread
from time import sleep

items = [2, 4, 5, 2, 1, 7]


def sleep_sort(i):
    sleep(i * 0.001)
    print(i)


l = [Thread.start_new_thread(sleep_sort, (i,)) for i in items]
print(l)