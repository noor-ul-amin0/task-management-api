from fastapi import APIRouter, HTTPException
from app.models.task import Task
from app.managers.task_manager import TaskManager

router = APIRouter(prefix='/tasks', tags=['Tasks'])

task_manager = TaskManager()


@router.get("/")
def read_tasks(query: str | None = None):
    return {"success": True, "data": task_manager.get_tasks()}


@router.post('/')
def create_task(task: Task):
    new_task = task_manager.add_task(task)
    return {"success": True, "data": new_task}


@router.get('/{task_id}')
def read_task(task_id: str):
    task = task_manager.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"success": True, "data": task}


@router.put('/{task_id}')
def update_task(task_id: str, task: Task):
    updated_task = task_manager.update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"success": True, "data": updated_task}


@router.delete('/{task_id}')
def delete_task(task_id: str):
    deleted_task = task_manager.delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"success": True, "data": deleted_task}
