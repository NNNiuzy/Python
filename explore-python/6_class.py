class A(object):
    bar = 1
    @classmethod
    def class_foo(cls):
        print('hello,', cls)
        print(cls.bar)
