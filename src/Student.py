from src.Person import Person
class Student(Person):
    def __init__(self, name, family, student_id):
        super().__init__(name, family)
        self.student_id = student_id
        self.lectures = []
        self.grades = {}
    
    def Compute_average_grade(self):

        return float(sum(self.grades.values())/len(self.lectures))
     
    def pick_lecture(self,lecture_name):
        try:
            self.lectures.append(lecture_name)
            if lecture_name not in self.grades:
                self.grades[lecture_name] = None
        except Exception as e:
            print(f"Error picking lecture: {e}")

    def Status(self):
        try:
            if self.Compute_average_grade > 12:
                return 'Pass'
            else:
                return 'Fail'
        except:
            print('Invalid Grade')

    def to_dict(self):
        return {
            'name' : self.name,
            'family': self.family,
            'student_id' : self.student_id,
            'grades' : self.grades,
            'average_grade': self.Compute_average_grade(),
            'staus' : self.Status(),
            'lectures' : self.lectures
        }


