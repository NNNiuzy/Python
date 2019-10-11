# from threading import Thread, current_thread
#
#
# def echo(num):
#     print(current_thread().name, num)
#
#
# def calc():
#     print("thread %s is running" % current_thread().name)
#     local_num = 0
#     for _ in range(10000):
#         local_num += 1
#     echo(local_num)
#     print("thread %s ended" % current_thread().name)
#
#
# if __name__ == '__main__':
#     print("thread %s is running" % current_thread().name)
#
#     thread = []
#     for i in range(5):
#         thread.append(Thread(target=calc))
#         thread[i].start()
#     for i in range(5):
#         thread[i].join()
#     print("thread %s is ended" % current_thread().name)
#
#
# from threading import Thread, current_thread
#
# global_dict = {}
#
#
# def echo():
#     num = global_dict[current_thread()]
#     print(current_thread().name, num)
#
#
# def calc():
#     print("thread %s is running" % current_thread().name)
#     global_dict[current_thread()]=0
#     for _ in range(10000):
#         global_dict[current_thread()] += 1
#     echo()
#     print("thread %s ended" % current_thread().name)
#
#
# if __name__ == '__main__':
#     print("thread %s is running" % current_thread().name)
#
#     thread = []
#     for i in range(5):
#         thread.append(Thread(target=calc))
#         thread[i].start()
#     for i in range(5):
#         thread[i].join()
#     print("thread %s is ended" % current_thread().name)




from threading import Thread, current_thread, local


global_data = local()


def echo():
    num = global_data.num
    print(current_thread().name, num)


def calc():
    print("thread %s is running" % current_thread().name)
    global_data.num = 0
    for _ in range(10000):
        global_data.num += 1
    echo()
    print("thread %s ended" % current_thread().name)


if __name__ == '__main__':
    print("thread %s is running" % current_thread().name)

    threads = []
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].start()
    for i in range(5):
        threads[i].join()
    print("thread %s is ended" % current_thread().name)
