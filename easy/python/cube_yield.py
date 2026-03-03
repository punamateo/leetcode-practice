


def cube_yield(n):
    for i in range(n):
        yield i ** 3


cube = cube_yield(10)


for i in cube:
    print(i)
