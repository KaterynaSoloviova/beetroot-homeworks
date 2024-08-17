# ask 1
# A Person class
# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them
# as attributes. Make another method called talk() which makes prints a greeting from the person containing,
# for example like this:
# "Hello, my name is Carl Johnson and I’m 26 years old"

class Person:
    def __init__(self, fist_name: str, last_name: str, age: int) -> None:
        self.first_name = fist_name
        self.last_name = last_name
        self.age = age

    def talk(self) -> None:
        print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old")


object = Person("John", "Smith", "18")
object.talk()
