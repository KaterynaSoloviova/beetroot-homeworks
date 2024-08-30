# Custom exception
# Create your custom exception named CustomException, you can inherit from base Exception class, but extend
# its functionality
# to log every error message to a file named logs.txt. Tips: Use __init__ method to extend functionality for
# saving messages to file

class CustomException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        with open("logs.txt", "a") as log_file:
            log_file.write(f"Error: {msg}\n")


try:
    raise CustomException("Something went wrong!")
except CustomException as err:
    print(err)

