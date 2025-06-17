from functools import wraps


def validate_positive(func):

    @wraps(func)
    def wrapper(*args):
        if all([arg > 0 for arg in args]):
            return func(*args)
        raise ValueError("Все аргументы должны быть положительными")

    return wrapper
