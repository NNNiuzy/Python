def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("numbers:", numbers)
    return sum

print(add(1,2))