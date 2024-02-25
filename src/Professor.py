from src.Person import Person
from src.Student import Student
class Professor(Person):
    def __init__(self, name, family, professor_id):
        super().__init__(name, family)
        self.professor_id = professor_id
        self.courses = []

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'type': 'Professor',
            'professor_id': self.professor_id,
            'lectures': self.lectures
        })
        return data
    
    # def save_data_to_json(file_path, data):
    #     with open(file_path, 'w') as file:
    #         json.dump(data, file, indent=4)

    # def load_data_from_json(file_path):
    #     with open(file_path, 'r') as file:
    #         data = json.load(file)
    #     return data
    
    def assign_grade(self,student,lecture_name,grade):
        if isinstance(student, Student) and lecture_name in student.lectures:
            student.grades[lecture_name] = grade
            
    def choose_course(self,course_name):
        if len(self.courses) < 3:
            self.courses.append(course_name)
        else:
            print("Can not choose more than 3 courses.")
      
    def __repr__(self):
        return f"professor {self.name} {self.family}\tID {self.professor_id}"
            
        



