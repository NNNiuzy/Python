# def counter(start=0):
#     def incr():
#         nonlocal start
#         start += 1
#         return start
#
#     return incr
#
#
# c1 = counter(5)
# print(c1())
# print(c1())
#
# c2 = counter(50)
# print(c2())
# print(c2())
#
# print(c1())
# print(c1())
#
# print(c2())

# from math import sqrt
#
# class Point(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def get_instance(self,u,v):
#         distance = sqrt((self.x-u)**2+(self.y-v)**2)
#         return distance

# def count():
#     funcs = []
#     for i in range(1,4):
#         def f():
#             return i
#
#         funcs.append(f)
#     return funcs

def count():
    funcs = []
    for i in range(1, 4):
        def g(param):
            f = lambda : param
            return f

        funcs.append(g(i))
    return funcs