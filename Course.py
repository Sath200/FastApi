from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Course(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    author: Optional[str] = None


app = FastAPI()
courses = []


@app.post("/courses")
def create_course(course: Course):
    courses.append(course)
    return course


@app.get("/courses")
def get_course():
    return courses


@app.delete("/courses/{name}")
def del_course(name: str):
    for i in courses:
        if i.name == name:
            courses.remove(i)
    return courses


@app.put("/courses/{name}")
def update_course(name: str, course: Course):
    for i in courses:
        if i.name == name:
            i.description = course.description
            i.price = course.price
            i.author = course.author
    return courses
