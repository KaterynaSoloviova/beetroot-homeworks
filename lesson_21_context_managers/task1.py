# Task 1
# File Context Manager class
# Create your own class, which can behave like a built-in function open(). Also, you need to extend its functionality
# with counter and logging. Pay special attention to the implementation of __exit__ method, which has to cover all the
# requirements to context managers
from io import TextIOWrapper

class OpenFileManager:
    file_open_counter = 0

    def __init__(self, file_name: str, mode: str = "r") -> None:
        self.file_name: str = file_name
        self.mode: str = mode
        self.file: TextIOWrapper | None = None
        self.log(f"Initialized OpenFileManager for {self.file_name} in {self.mode} mode")

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mode)
            OpenFileManager.file_open_counter += 1
            self.log(f"Opened file: {self.file_name}")
            return self.file
        except Exception as e:
            self.log(f"Failed to open file: {self.file_name} - Error: {e}")
            raise

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            try:
                self.file.close()
                self.log(f"Closed file: {self.file_name}")
            except Exception as e:
                self.log(f"Error while closing file: {self.file_name} - Error: {e}")
        if exc_type:
            self.log(f"An exception occurred: {exc_type.__name__}: {exc_value}")
            return False

    @staticmethod
    def log(message):
        print(f"[LOG] {message}")

    @classmethod
    def get_open_counter(cls):
        return cls.file_open_counter


# Writing to a file
with OpenFileManager('test.txt', 'w') as file:
    file.write("Hello, World!")

# Reading from a file
with OpenFileManager('test.txt', 'r') as file:
    content = file.read()
    print(content)

# Check how many times files were opened
print(f"Total file accesses: {OpenFileManager.get_open_counter()}")
