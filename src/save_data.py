import json
from src.Student import Student
def save_all_students_data(students):
    data = [Student.to_dict(student) for student in students]
    with open("data.json","w") as file:
        json.dump(data, file , indent=4)