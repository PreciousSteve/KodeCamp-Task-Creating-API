# PROMOTIONAL TASK 5

from fastapi import FastAPI, Path, Query, HTTPException
from typing import Annotated

app = FastAPI()


# TASK 1

# Number Range Validator API:
# Create an API that checks if a given number (path parameter) falls within a specified range.
# Example: /validate_number/5?min=1&max=10 → True

@app.get('/number/{given_number}')
def range_validator(given_number:Annotated[int, Path()], min:Annotated[int, Query()], max:Annotated[int, Query()]):
    if given_number >= min and given_number <= max:
        return True
    else:
        return False


# TASK 2

# Simple Arithmetic API:
# Build an API that performs basic arithmetic operations (add, subtract, multiply, divide) using path parameters.
# Example: /add/3/5 → 8

@app.get('/add/{first_num}/{second_num}')
def addition(first_num:Annotated[int, Path()], second_num:Annotated[int, Path()]):
    response = first_num + second_num
    return{"result":f"{response}"}

@app.get('/subtract/{first_num}/{second_num}')
def subtraction(first_num:Annotated[int, Path()], second_num:Annotated[int, Path()]):
    response = first_num - second_num
    return{"result":f"{response}"}

@app.get('/multiply/{first_num}/{second_num}')
def multiplication(first_num:Annotated[int, Path()], second_num:Annotated[int, Path()]):
    response = first_num * second_num
    return{"result":f"{response}"}

@app.get('/divide/{first_num}/{second_num}')
def division(first_num:Annotated[int, Path()], second_num:Annotated[int, Path()]):
    response = first_num / second_num
    return{"result":f"{response}"}


# TASK 3

# Todo List API:
# Develop an API to manage a simple to-do list with endpoints to add, view, and delete tasks.
# Use request body to add tasks and path parameters to identify tasks.
# Example: POST /tasks with request body { "task": "Buy groceries" }

from pydantic import BaseModel


class Tasks(BaseModel):
    task: str
    

tasks = []

@app.post("/tasks")
def add_task(task: Tasks):
    tasks.append(task)
    return tasks

@app.get("/view-tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{id}")
def delete_task(id: int):
    if id in tasks:
        tasks.remove(id)
        return {"message": "Task deleted successfully"}
        raise HTTPException(status_code=404, detail="Task not found")


# TASK 4

# String Length API:
# Create an API that takes a string as a query parameter and returns its length.
# Example: /length?text=hello → 5

@app.get('/string')
def know_length(text:Annotated[str, Query()]):
    length = len(text)
    return {"text":f" The length is {length}"}



# TASK 5

# Age Checker API:
# Build an API that checks if a user is an adult based on their age provided as a path parameter.
# Example: /check_age/20 → "Adult" or "Not an adult

@app.get('/check-age/{age}')
def age_check(age:Annotated[int, Path()]):
    if age >= 18:
        return {"age":f" Adult"}
    else:
        return {"age":f"Not an adult"}
    


# TASK 6

# Square Number API:
# Develop an API that returns the square of a number provided as a path parameter.
# Example: /square/4 → 16

@app.get('/square/{num}')
def get_square(num:Annotated[int, Path()]):
    square = num * num
    return {"num":f"The square of {num} is {square}"}



# TASK 7

# BMI Calculator API:
# Create an API that calculates BMI based on weight and height provided in the request body.
# Example: POST /bmi with request body { "weight": 70, "height": 1.75 }

class BMI(BaseModel):
    weight:float
    height:float

@app.post('/bmi')
def calculate_bmi(calculate:BMI):
    # Your BMI is calculated by dividing your weight by your height squared.
    bmi = calculate.weight/(calculate.height*calculate.height)
    return f"Your BMI is {bmi}"



# TASK 8

# Simple Interest Calculator API:
# Create an API that calculates simple interest based on principal, rate, and time provided in the request body.
# Example: POST /interest with request body { "principal": 1000, "rate": 5, "time": 2 }
class SI(BaseModel):
    principal: int
    rate: int
    time: int

@app.post('/simple-interest')
def cal_SI(cal:SI):
    simple_interest = (cal.principal * cal.rate * cal.time)/100
    return simple_interest



# TASK 9

# Temperature Converter API:
# Build an API that converts temperatures between Celsius and Fahrenheit using query parameters.
# Example: /convert_temp?temp=100&unit=celsius → 212

@app.get('/convert-temp')
def convert(temp:Annotated[float, Query()], unit:Annotated[str, Query()]):
    if unit == "celsius":
        return (temp - 32) * 5 / 9
    elif unit == "fahrenhiet":
        return (temp * 9 / 5) + 32
    else:
        return f"Error"
    

# TASK 10


# Random Number Generator API:
# Develop an API that returns a random number between a given range provided as query parameters.
# Example: /random?min=1&max=100 → 42

import random

@app.get('/random-num')
def get_number(min:Annotated[int, Query], max:Annotated[int, Query]):
    random_number = random.randint(min, max)
    return random_number