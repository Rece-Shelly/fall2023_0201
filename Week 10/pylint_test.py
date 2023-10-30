class Student():
    def __init__(self, first_name, last_name, student_id=0):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id
    
    def getStudentId(self):
        return self.__student_id

student_1 = Student("Kamil", "Akhuseyinoglu")


