# Task 3
# Write a decorator arg_rules() that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules(' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.)
import functools


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            param = args[0]
            if type(param) != type_:
                print("Incorrect type")
                return False
            if len(param) > max_length:
                print("Incorrect length")
                return False
            for element in contains:
                if element not in param:
                    print(f"Element '{element}' is not present")
                    return False
            result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
