from time import time, sleep
from functools import reduce


def slowit(sleep_time=1):
    def wrapper(func):
        def inner(*args, **kwargs):
            sleep(sleep_time)
            return func(*args, **kwargs)
        return inner

    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        print(f'Time for work: {time_end - time_start:.6f}')
        return result
    return wrapper


def memoize(func):
    cache = {}  # Словарь для хранения результатов

    def wrapper(*args):
        if args in cache:  # Если результат уже есть в кэше
            return cache[args]
        result = func(*args)  # Иначе вычисляем
        cache[args] = result  # Сохраняем в кэш
        return result

    return wrapper



# Без кеширования время работы функции при каждом вызове не менее 2 секунд.
@timeit
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

product(10)
product(10)

# С кешированием время работы функции при первом вызове не менее 2 секунд, при втором вызове почти мгновенно.
@timeit
@memoize
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else None

product(10)
product(10)