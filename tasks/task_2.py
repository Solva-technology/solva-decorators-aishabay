from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            print("Из кэша")
        else:
            cache[args] = func(*args, **kwargs)
        return cache.get(args)

    return wrapper
