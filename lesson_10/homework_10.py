from abc import ABC, abstractmethod

# task_1
class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)


class Developer(Employee):
    def __init__(self, programming_language=None, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)


class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)

Sasha_1 = TeamLead(name="Natan", salary=30000, department='Sale', team_size=33)
print(Sasha_1.name)
print(Sasha_1.department)
print(Sasha_1.team_size)
print(TeamLead.mro())



# task2




class Figure(ABC):

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, a):
        self.a = a
    def square(self):
        s = self.a*self.a
        return s
    def perimeter(self):
        p = self.a*4
        return p

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        s = self.a*self.b
        return s
    def perimeter(self):
        p = (self.a+self.b)*2
        return p

class Triangle(Figure):
    def __init__(self, a, b, c, h):
        self.a = a
        self.h = h
        self.b = b
        self.c = c
    def square(self):
        s = self.a*self.h/2
        return s
    def perimeter(self):
        p = self.a+self.b+self.c
        return p

sq_f = Square(3)
tr_f = Triangle(4, 5, 6, 7)
rectangle = Rectangle(3,4)

for f in [sq_f, tr_f, rectangle]:
    print(f.square())

for f in [sq_f, tr_f, rectangle]:
    print(f.perimeter())

