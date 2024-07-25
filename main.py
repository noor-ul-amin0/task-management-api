from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from utils import generate_id
from utils import get_current_date
from tasks import tasks

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str

@app.get("/tasks")
def read_tasks():
    return {"success": True, "data": tasks}

@app.get('/tasks/{task_id}')
def read_task(task_id: str):
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
    return {"success": True, "data": task}


@app.post('/tasks')
def create_task(task: Task):
    new_task = {
        "id": generate_id(),
        "title": task.title,
        "description": task.description,
        "completed": False,
        "created_at": get_current_date(),
        "updated_at": get_current_date(),
    }
    tasks.append(new_task)
    return {"success": True, "data": new_task}

@app.put('/tasks/{task_id}')
def update_task(task_id: str, task: Task):
    updated_task = None
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = task.title
            t["description"] = task.description
            t["completed"] = task.completed
            t["updated_at"] = get_current_date()
            updated_task = t
    return {"success": True, "data": updated_task}

@app.delete('/tasks/{task_id}')
def delete_task(task_id: str):
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            tasks.remove(t)
    return {"success": True, "data": task}