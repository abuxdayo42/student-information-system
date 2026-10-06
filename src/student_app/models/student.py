class Student:
    def __init__(self, student_id, name, program, semester, marks):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.semester = semester
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def update_semester(self, new_semester):
        self.semester = new_semester