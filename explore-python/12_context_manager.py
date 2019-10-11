# from math import sqrt, pow
#
#
# class Point(object):
#     def __init__(self, x, y):
#         print('initialize x and y')
#         self.x, self.y = x, y
#
#     def __enter__(self):
#         print('Entering context')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting context")
#
#     def get_distance(self):
#         distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
#         return distance
#
#
# # with Point(3, 4) as pt:
# #     print('distance: ', pt.get_distance())
#
#
# with Point(3, 4) as pt:
#     pt.get_length()


# from math import sqrt, pow
#
#
# class Point(object):
#     def __init__(self, x, y):
#         print('initialize x and y')
#         self.x, self.y = x, y
#
#     def __enter__(self):
#         print('Entering context')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exception has been handled')
#         print("Exiting context")
#         return True
#
#     def get_distance(self):
#         distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
#         return distance
#
#
# with Point(3,4) as pt:
#     pt.get_length()


from contextlib import contextmanager


@contextmanager
def point(x, y):
    print('before yield')
    yield x * x + y * y
    print('after yield')


with point(3, 4) as value:
    print('value is: %s' % value)
