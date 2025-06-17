from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_kwargs = (*args, frozenset(kwargs.values()))
        if args_kwargs in cache:
            print("Из кэша")
        else:
            cache[args_kwargs] = func(*args, **kwargs)
        return cache.get(args_kwargs)

    return wrapper
