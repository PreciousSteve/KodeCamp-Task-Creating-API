from fastapi import FastAPI, Form, HTTPException, UploadFile, Depends
from PIL import Image

app = FastAPI()


# Contact Form API:
# Create an API to handle contact form submissions. 
# Use form data to receive input from users and error handling to validate required fields, returning appropriate status codes for missing or invalid data.
from typing import Annotated

@app.post("/add-contact")
def contact(first_name:Annotated[str, Form()], last_name:Annotated[str, Form()], phone_number:Annotated[str, Form(min_length=11, max_length=11)],age:Annotated[int, Form()]):
    if not first_name:   # if not: checks if first_name is None or an empty string
        raise HTTPException(status_code=422, detail="Required Field")
    if not last_name:
        raise HTTPException(status_code=422, detail="Required Field")
    if not phone_number:
        raise HTTPException(status_code=422, detail="Required Field")
    if not age:
        raise HTTPException(status_code=422, detail="Required Field")
    return {"message":f'Thank You, {first_name} {last_name}!'}
 

# Profile Picture Upload API:
# Develop an API that allows users to upload profile pictures. 
# Use request files to handle image uploads and dependencies to validate image dimensions and formats, with error handling for invalid submissions.

def validate_pic(picture:UploadFile):
    allowed_formats = ["image/jpeg", "image/png"]
    min_width = 400
    min_height = 500
    if picture.content_type not in allowed_formats:
        raise HTTPException(status_code=400, detail="Invalid image format. Only JPEG and PNG are allowed.")
    # Opening the image file
    img = Image.open(picture.file)
    # Checking the image dimensions
    if img.width < min_width or img.height < min_height:
        raise HTTPException(status_code=400, detail="Minimum dimensions are 400x500 pixels!")
    # Checking the image format
    if img.format not in ["JPEG", "PNG"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG formats are allowed!")
    return img

    
@app.post("/profile-pic")
def upload_pic(picture:UploadFile=Depends(validate_pic)):
    try:
        return {"message": f"Uploaded successfully!{picture}"}
    except HTTPException as e:
        return {"error": e.detail}



# Multi-Part Form Data API:
# Create an API that accepts multi-part form data, such as a form with both text and file inputs 
# (e.g., a job application form with resume uploads). Use dependencies to validate inputs and error handling for missing or invalid data.

def check_inputs(first_name, last_name, qualification, resume):
    if not first_name:
        raise HTTPException(status_code=422, detail= "Put your first name")
    if not last_name:
        raise HTTPException(status_code=422, detail= "Put your last name")
    if qualification != "Bsc" and qualification != "Msc":
        raise HTTPException(status_code=422, detail= "Only Bsc or Msc Qualification needed")
    if not resume:
        raise HTTPException(status_code=422, detail= "Put your resume")
    
    
@app.post("/fill-form")
def fill_form(first_name:Annotated[str, Form()], last_name:Annotated[str, Form()], qualification:Annotated[str, Form()], resume:UploadFile):
    check_inputs(first_name, last_name, qualification, resume)
    return {"message":"Application Recieved"}
 

# Simple Calculator API:
# Create an API that performs basic arithmetic operations (addition, subtraction, multiplication, division).
#  Use dependencies to manage and validate input parameters.

def valid_input(first_num, second_num):
    if type(first_num) != int:
        raise HTTPException(status_code=422, detail="Number should be integer")
    if type(second_num) != int:
        raise HTTPException(status_code=422, detail="Number should be integer")

@app.get('/addition/{first_num}/{second_num}')
def addition(first_num:int, second_num:int):
    valid_input(first_num, second_num)
    response = first_num + second_num
    return{"result":f"{response}"}

@app.get('/subtraction/{first_num}/{second_num}')
def subtraction(first_num:int, second_num:int):
    valid_input(first_num, second_num)
    response = first_num - second_num
    return{"result":f"{response}"}

@app.get('/multiplication/{first_num}/{second_num}')
def multiplication(first_num:int, second_num:int):
    valid_input(first_num, second_num)
    response = first_num * second_num
    return{"result":f"{response}"}

@app.get('/division/{first_num}/{second_num}')
def division(first_num:int, second_num:int):
    valid_input(first_num, second_num)
    try:
        response = first_num / second_num
    except:
        raise HTTPException(status_code=422, detail="no Number cannot not be 0")
    return{"result":f"{response}"}



# Todo List API:
# Build an API to manage a simple to-do list. Use dependencies to handle the storage and retrieval of tasks.

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    task_to_do: str

tasks = []


def create_task(task: Task):
    tasks.append(task)
    return task

def get_tasks():
    return tasks


@app.post("/tasks")
def create_tasks(task: Task):
    return create_task(task)


@app.get("/tasks")
def read_tasks():
    return get_tasks()






