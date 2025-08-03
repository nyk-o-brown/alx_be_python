
class student:
    def __init__(self, name , course, grade):
        self.name = name
        self.course = course
        self.grade = grade
    
    def show_data(self) :
        print(f"{self.name} is enroled in {self.course} and has a grade of {self.grade}")    