# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def make_greeting_with_position(position):
    def greeting(name):
        print(f'Hello my name is  {name}. I am a {position}')

    return greeting


student_greeting = make_greeting_with_position("student")
teacher_greeting = make_greeting_with_position("teacher")

student_greeting("Yurii")
student_greeting("Kate")
student_greeting("Bob")
student_greeting("Vova")
teacher_greeting("Sashko")
