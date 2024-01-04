import uvicorn
from fastapi import FastAPI, Path        #get = get an information
from pydantic import BaseModel
from typing import Optional               #post = create something new
app = FastAPI()                          #put = update
                                         #delete = delete something
students = {
    1: {
        "name": "Jack",
        "age": 18,
        "year": "year 15"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class Update_student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")  #gt = greater than, ge = greater than / equal same with lt,le also
def get_student(student_id: int = Path(description = "The ID of the student you want to view", gt = 0, lt = 3)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(student_id: int, name: str | None = None): #or we can do directly none
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id]= student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Update_student):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year


    return students[student_id]

if __name__ == "__main__":
    uvicorn.run("student_info_FastAPI:app", reload=True)
