import json
from src.Student import Student
from src.Person import Person
from src.Professor import Professor
from src.save_data import save_all_students_data

def main():
    students = []  # List to hold student instances

    professor = Professor("John", "Doe","P1000")
    professor.choose_course("Math")
    professor.choose_course("Science")
    professor.choose_course("History")

    # Create and configure students
    student1 = Student("Jane", "Doe", "S1234")
    student1.pick_lecture("Math")
    student1.pick_lecture("Science")
    professor.assign_grade(student1, "Math", 16)
    professor.assign_grade(student1, "Science", 17)

    student2 = Student("Mike", "Smith", "S5678")
    student2.pick_lecture("Math")
    student2.pick_lecture("History")
    professor.assign_grade(student2, "Math", 18)
    professor.assign_grade(student2, "History", 19)

    # Add students to the list
    students.append(student1)
    students.append(student2)

    # Save all students' data to data.json
    save_all_students_data(students)

main()