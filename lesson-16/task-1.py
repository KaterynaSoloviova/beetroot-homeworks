# Task 1
# School
# Make a class structure in python representing people at school. Make a base class called Person, a class called
# Student, and another one called Teacher. Try to find as many methods and attributes as you can which belong to
# different classes, and keep in mind which are common and which are not. For example, the name should be a Person
# attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, first_name: str, last_name: str, position: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def greeting(self) -> None:
        print(f"Hello, my name is {self.first_name} {self.last_name}. I am a {self.position} in this school.")


class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int, grade_level: int) -> None:
        super().__init__(first_name, last_name, "student")
        self.age = age
        self.grade_level = grade_level
        self.is_busy = True
        self.level_exam_preparation = 0

    def greeting(self) -> None:
        super().greeting()
        print(f"I am {self.age} old years and I am a {self.grade_level}-grade student")

    def pass_exams(self) -> None:
        if self.level_exam_preparation >= 70:
            self.is_busy = False
            print(f"{self.first_name}: Hooray! I passed the exams successfully!🥳")
        else:
            print(f"{self.first_name}: Oops! I failed the exams!😭")

    def go_to_cinema(self) -> None:
        if self.is_busy:
            print(f"{self.first_name}: I can't go to the cinema because I have to prepare for my exams.")
        else:
            print(f"{self.first_name}: Let's go to the cinema!")

    def go_to_the_library(self):
        self.level_exam_preparation += 30
        if self.level_exam_preparation > 100:
            self.level_exam_preparation = 100
        print(f"{self.first_name}: I am going to the library!.")


class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, teaching_time: int, subject: str, salary: int) -> None:
        super().__init__(first_name, last_name, "teacher")
        self.teaching_time = teaching_time
        self.subject = subject
        self.salary = salary
        self.money = 0

    def greeting(self) -> str:
        super().greeting()
        print(f"I have been teaching a {self.subject} at this school for {self.teaching_time} years.")

    def get_salary(self) -> int:
        self.money += self.salary
        print(f"{self.first_name}: I have the salary of {self.salary} euro. Now I have {self.money} euro.")

    def go_to_vacation(self) -> bool:
        can_go = self.money >= 2000
        if can_go:
            self.money -= 2000
            print(f"{self.first_name}: Finally, I can afford to go on holiday!")
        else:
            print(f"{self.first_name}: Oh no, I need to work harder to go on holiday!")
        return can_go


teacher_physics = Teacher("John", "Doe", 15, "physics", 1000)
teacher_physics.greeting()
student_mary = Student("Mary", "Shelley", 12, 9)
student_jens = Student("Jens", "Fisher", 10, 7)
student_mary.greeting()
student_jens.greeting()

student_jens.go_to_the_library()
student_mary.go_to_the_library()
student_jens.go_to_the_library()
student_mary.go_to_the_library()
student_jens.go_to_the_library()
student_jens.go_to_the_library()
student_mary.pass_exams()
student_mary.go_to_cinema()
student_mary.go_to_the_library()
student_mary.pass_exams()
student_jens.pass_exams()
student_mary.go_to_cinema()
student_jens.go_to_cinema()
teacher_physics.get_salary()
if not teacher_physics.go_to_vacation():
    teacher_physics.get_salary()
    teacher_physics.go_to_vacation()
