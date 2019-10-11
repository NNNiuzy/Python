# def generator_function():
#     print('hello 1')
#     yield 1
#     print('hello 2')
#     yield 2
#     print('hello 3')

# def fib():
#     a, b = 0, 1
#     while True:
#         a, b = a + b, a
#         yield a
#
#
# f = fib()
# for item in f:
#     if item > 10:
#         break
#     print(item)


def generator_function():
    value1 = yield 0
    print('value1 is ', value1)
    value2 = yield 1
    print('value2 is ', value2)
    value3 = yield 2
    print('value3 is ', value3)

g = generator_function()
