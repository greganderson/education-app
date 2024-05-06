from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from database import get_db
from models import Course, Instructor, Student


app = FastAPI()


### GET ###

@app.get("/students")
async def get_students(db: Session = Depends(get_db)) -> list[Student]:
    return db.exec(select(Student)).all()

@app.get("/instructors")
async def get_instructors(db: Session = Depends(get_db)) -> list[Instructor]:
    return db.exec(select(Instructor)).all()

@app.get("/courses")
async def get_courses(db: Session = Depends(get_db)) -> list[Course]:
    return db.exec(select(Course)).all()

@app.get("/courses/{course_id}/students")
async def get_course_student_list(course_id: int, db: Session = Depends(get_db)) -> list[Student]:
    statement = select(Course).where(Course.course_id == course_id)
    course = db.exec(statement).first()
    return course.students


### POST ###

@app.post("/students")
async def create_student(student: Student, db: Session = Depends(get_db)) -> None:
    db.add(student)
    db.commit()

@app.post("/instructors")
async def create_instructor(instructor: Instructor, db: Session = Depends(get_db)) -> None:
    db.add(instructor)
    db.commit()

@app.post("/courses")
async def create_course(course: Course, db: Session = Depends(get_db)) -> None:
    db.add(course)
    db.commit()

@app.post("/courses/{course_id}/students/{student_id}")
async def add_student_to_course(course_id: int, student_id: int, db: Session = Depends(get_db)) -> None:
    statement = select(Student).where(Student.student_id == student_id)
    student = db.exec(statement).first()

    statement = select(Course).where(Course.course_id == course_id)
    course = db.exec(statement).first()

    course.students.append(student)
    db.commit()