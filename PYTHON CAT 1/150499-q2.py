
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Grades: {student.grades}")

    def get_average_grade(self, name):
        for student in self.students:
            if student.name == name:
                return sum(student.grades.values()) / len(student.grades)
        return None

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return None
        return total / count

classroom = Classroom()
classroom.add_student(Student("Paul", {"Cost Accounting": 80, "API": 90, "Calculus":85}))
classroom.add_student(Student("Mary", {"Cost Accounting": 70, "API": 85, "Calculus":50}))
classroom.display_students()
print(f"Average Subject Grade:{classroom.get_average_grade("Paul")}")
print(f"Class Average:{classroom.get_class_average("API")}")

