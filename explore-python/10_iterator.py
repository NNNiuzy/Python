from collections import Iterator


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


if __name__ == '__main__':
    fib = Fib()
    print('isinstance(fib, Iterator):', isinstance(fib, Iterator))
    for i in fib:
        if i > 10:
            break
        print(i)
