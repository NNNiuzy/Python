# def makeitalic(func):
#     def wrapped():
#         return "<i>" + func() + "</i>"
#     return wrapped
#
# @makeitalic
# def hello():
#     return "hello world"


from functools import wraps


class Tag(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return "<{tag}>{res}</{tag}>".format(
                res=func(*args, **kwargs), tag=self.tag
            )

        return wrapped


@Tag('b')
def hello(name):
    return 'hello %s' % name
