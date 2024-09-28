# Task 2
# Writing tests for context manager
# Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use
# cases as you can, positive ones when a file exists and everything works as designed. And also, write tests when your
# class raises errors or you have errors in the runtime context suite.

from task1 import OpenFileManager
import unittest


class TestOpenFileManager(unittest.TestCase):
    def test_file_writing(self):
        with OpenFileManager('test.txt', 'w') as file:
            file.write("Hello, World!")
        with OpenFileManager('test.txt', 'r') as file:
            text = file.read()
        self.assertEqual(text, "Hello, World!")

    def test_file_writing_in_mode_read(self):
        with self.assertRaises(Exception) as ctx:
            with OpenFileManager('test.txt', 'r') as file:
                file.write("Hello, World!")
        self.assertEqual(str(ctx.exception), "not writable")

    def test_file_writing_with_error(self):
        with self.assertRaises(Exception) as ctx:
            with OpenFileManager('test2.txt', 'w') as file:
                file.write("Hello, World!")
                raise EnvironmentError("Something went wrong")
        self.assertEqual(str(ctx.exception), "Something went wrong")

        with OpenFileManager('test2.txt', 'r') as file:
            text = file.read()
        self.assertEqual(text, "Hello, World!")

    def test_file_append_mode(self):
        with OpenFileManager('test.txt', 'w') as file:
            file.write("Hello, ")
        with OpenFileManager('test.txt', 'a') as file:
            file.write("World!")
        with OpenFileManager('test.txt', 'r') as file:
            text = file.read()
            self.assertEqual(text, "Hello, World!")

    def test_not_existing_file(self):
        with self.assertRaises(FileNotFoundError) as ctx:
            with OpenFileManager('NonExisting.txt', 'r') as file:
                file.read()
        self.assertEqual(str(ctx.exception), "[Errno 2] No such file or directory: 'NonExisting.txt'")
