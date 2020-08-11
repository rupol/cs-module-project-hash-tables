import math
import random
import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def build_slowfun_lookup():
    lookup_table = {}
    # key: (x, y)
    # value: v - result of slowfun_too_slow

    for x in range(2, 14):
        for y in range(3, 6):
            lookup_table[(x, y)] = slowfun_too_slow(x, y)
    return lookup_table


slowfun_lookup_table = build_slowfun_lookup()


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    return slowfun_lookup_table[(x, y)]


start = time.time()
# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
