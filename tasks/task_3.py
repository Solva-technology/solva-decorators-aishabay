from functools import wraps


def validate_positive(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if all([arg > 0 for arg in args]) and all([kwarg > 0 for kwarg in kwargs]):
            return func(*args, **kwargs)
        raise ValueError("Все аргументы должны быть положительными")

    return wrapper
