from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load student data from the JSON file
def load_student_data():
    with open("q-vercel-python.json", "r") as file:
        data = json.load(file)
    return data

# Helper function to get marks by name
def get_marks_by_name(names: List[str]):
    students_data = load_student_data()
    marks = []
    name_to_marks = {student['name']: student['marks'] for student in students_data}
    for name in names:
        marks.append(name_to_marks.get(name, None))  # Return None if name not found
    return marks

# API route to return marks of students based on query parameters
@app.get("/api")
async def get_student_marks(name: List[str] = Query(...)):
    marks = get_marks_by_name(name)
    return JSONResponse(content={"marks": marks})
