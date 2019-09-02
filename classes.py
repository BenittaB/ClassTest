class Student:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender
        self.courses = {}

    def add_course(self, course, grades=[]):
        """Adds a course to a student's courses."""
        self.courses[course] = grades

    def __repr__(self):
        return self.name + " is " + str(self.age) + " old and is " + self.gender + "."


student1 = Student(14, "Pesho", "Female")
student2 = Student(13, "Mariika", "Female")
student3 = Student(22, "Benittka", "Female")

print(student3)
print(student3.courses)

student3.add_course("Math")
student3.add_course("Bel", [2,4])

print(student3.courses)
