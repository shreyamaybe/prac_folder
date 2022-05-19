#python- oop
# grading/ assigning :16

class Student:
    def __init__(self, name, age, grade) :
        self.name= name
        self.age= age
        self.grade= grade  #0-10

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, cname, max_students):
        self.cname= cname
        self.max_students = max_students
        self.students =[]

    def add_students(self, students):
        if len(self.students)< self.max_students:
            self.students.append(students)
            return True
        return False

    def get_average_score(self):
        score=0
        for student in self.students:
            value += student.get_grade()
        return score/len(self.students)

s1= Student("shreya", 20, 9.05)
s2= Student("riya", 21, 8.5)
s3= Student("priya", 20, 7.2)

course1= Course("Maths", 2)
course2= Course("Physics", 5)


course2.add_students(s1)
course2.add_students(s3)
