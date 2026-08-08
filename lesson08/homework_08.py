class Student:
    def __init__(self, name, surname, age, avg_point):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_point = avg_point
    def change_avg_point(self, new_value):
        self.avg_point = new_value

my_student = Student(name='Oleg', surname='Michal', age=33, avg_point = 34 )
print(f'The average point of {my_student.name} is {my_student.avg_point}.')
my_student.change_avg_point(56)
print(f'The average point of {my_student.name} is {my_student.avg_point}.')