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