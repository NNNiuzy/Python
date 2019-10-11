# import os
# from multiprocessing import Process
#
#
# def child_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=child_proc, args=('test',))
#     print('Process will start.')
#     p.start()
#     p.join()
#     print('Process end.')


import os, time
from multiprocessing import Pool


def foo(x):
    print('Run task %s (pid:%s)...' % (x, os.getpid()))
    time.sleep(2)
    print('Task %s result is : %s' % (x, x * x))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(foo, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
