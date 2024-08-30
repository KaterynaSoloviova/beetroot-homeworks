# Task 3
# Write a class TypeDecorators which has several methods for converting results of functions to a specified type
# (if it's possible):
# methods:
# to_int
# to_str
# to_bool
# to_float
# Don't forget to use @wraps

from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except:
                raise (ValueError, TypeError)

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
