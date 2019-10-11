# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Foo object (name: %s)' % self.name
#     __repr__ = __str__


# print(Foo('Carl'))
# print(str(Foo('Carl')))
# Foo('Carl')
#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
#     def __getitem__(self, n):
#         if isinstance(n, slice):
#             a, b = 1, 1
#             start, stop = n.start, n.stop
#             L = []
#             for i in range(stop):
#                 if i >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#         if isinstance(n, int):
#             a, b = 1, 1
#             for i in range(n):
#                 a, b = b, a + b
#             return a


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattr__(self, attr):
        if attr == 'z':
            return 0
        raise AttributeError("Point object has no attribute %s" % attr)

    def __setattr__(self, *args, **kwargs):
        print('call func set attr (%s, %s)' % (args, kwargs))
        return object.__setattr__(self, *args, **kwargs)

    def __delattr__(self, *args, **kwargs):
        print('call func del attr (%s, %s)' % (args, kwargs))
        return object.__delattr__(self, *args, **kwargs)

    def __call__(self, z):
        return self.x + self.y + z
