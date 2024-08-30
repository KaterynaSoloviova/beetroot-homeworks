# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
import functools


def stop_words(words: list):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))
