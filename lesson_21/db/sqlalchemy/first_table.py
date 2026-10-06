import random
from faker import Faker
from sqlalchemy import create_engine, insert, delete
from sqlalchemy.orm import sessionmaker
from lesson_21.db.sqlalchemy.usertable import Base, Student, Course, student_course

fake = Faker()

# DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/dbname"
engine = create_engine("sqlite:///lesson21.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def seed():
    courses = [Course(title=t) for t in ["Python", "SQL", "Testing", "Linux", "Git"]]
    students = [
        Student(name=fake.name(), age=random.choice(range(18, 100)))
        for _ in range(20)
    ]
    session.add_all(courses + students)
    session.flush()

    rows = []
    for s in students:
        for c in random.sample(courses, k=random.randint(1, 3)):
            rows.append({"student_id": s.id, "course_id": c.id})
    session.execute(insert(student_course), rows)
    session.commit()


def add_student_to_course(name, age, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course is None:
        print(f"'{course_title}' not found")
        return None
    student = Student(name=name, age=age)
    session.add(student)
    session.flush()
    session.execute(insert(student_course).values(student_id=student.id, course_id=course.id))
    session.commit()
    return student


def get_students_by_course(course_title):
    return (
        session.query(Student)
        .join(student_course, Student.id == student_course.c.student_id)
        .join(Course, Course.id == student_course.c.course_id)
        .filter(Course.title == course_title)
        .all()
    )


def get_courses_by_student(student_id):
    return (
        session.query(Course)
        .join(student_course, Course.id == student_course.c.course_id)
        .filter(student_course.c.student_id == student_id)
        .all()
    )


def get_all_enrollments():
    return (
        session.query(Student.name, Course.title)
        .join(student_course, Student.id == student_course.c.student_id)
        .join(Course, Course.id == student_course.c.course_id)
        .order_by(Course.title)
        .all()
    )


def update_student(student_id, name=None, age=None):
    student = session.get(Student, student_id)
    if student is None:
        return None
    if name is not None:
        student.name = name
    if age is not None:
        student.age = age
    session.commit()
    return student


def update_course(course_id, new_title):
    course = session.get(Course, course_id)
    if course is None:
        return None
    course.title = new_title
    session.commit()
    return course


def delete_student(student_id):
    student = session.get(Student, student_id)
    if student is None:
        return False
    session.execute(delete(student_course).where(student_course.c.student_id == student_id))
    session.delete(student)
    session.commit()
    return True


if __name__ == "__main__":
    seed()
    jack = add_student_to_course("Jack", 21, "Python")
    print("New student:", jack)
    print("Courses Jack:", *get_courses_by_student(jack.id), sep="\n  ")
    print("\nStudents on 'Python':")
    print(*get_students_by_course("Python"), sep="\n")
    print("\nAll lists:")
    for name, title in get_all_enrollments():
        print(f"  {title}: {name}")
    print("\nUpdate:", update_student(1, name="Jack Updated", age=25))
    print("Update course:", update_course(5, "Git & GitHub"))
    print("\nDelete id=2:", delete_student(2))
    session.close()