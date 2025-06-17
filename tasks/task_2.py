from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if cache.get(func.__name__ + str(args)):
            print("Из кэша")
        else:
            cache[func.__name__ + str(args)] = func(*args)
        return cache.get(func.__name__ + str(args))

    return wrapper
