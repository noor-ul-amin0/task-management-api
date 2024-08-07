from typing import List, Optional
from app.models.task import Task
from app.utils.utils import generate_id, get_current_date


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> Task:
        task.id = generate_id()
        task.created_at = get_current_date()
        task.updated_at = get_current_date()
        self.tasks.append(task)
        return task

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_task(self, task_id: str) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: str, updated_task: Task) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                task.title = updated_task.title
                task.description = updated_task.description
                task.completed = updated_task.completed
                task.updated_at = get_current_date()
                return task
        return None

    def delete_task(self, task_id: str) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return task
        return None
