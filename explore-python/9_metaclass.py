# class Foo(object):
#     foo = True
#
#
# class Bar(object):
#     bar = True
#
#
# def echo(cls):
#     print(cls)
#
#
# def select(name):
#     if name == 'foo':
#         return Foo
#     if name == 'bar':
#         return Bar


# class Foo(object):
#     foo = True
#
#     def greet(self):
#         print('hello world')
#         print(self.foo)


# def greet(self):
#     print('hello world')
#     print(self.foo)
#
#
# Foo = type('Foo', (object,), {'foo': True, 'greet': greet})


class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 给所有的属性和方法前面加上前缀 my_
        _attrs = (('my_' + name, value) for name, value in attrs.items())

        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加了一个echo方法
        return type.__new__(cls, name, bases, _attrs)  # 返回创建后的类


class Foo(metaclass=PrefixMetaclass):
    name = 'foo'

    def bar(self):
        print('bar')


class Bar(Foo):
    prop = 'bar'
