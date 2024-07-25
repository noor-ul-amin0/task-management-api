from utils import generate_id

tasks = [
    {
        "id": generate_id(),
        "title": "Create a new project",
        "description": "Create a new project using FastAPI",
        "completed": False,
        "created_at": "2021-09-01T12:00:00",
        "updated_at": "2021-09-01T12:00:00"
    },
    {
        "id": generate_id(),
        "title" : "Take out the trash",
        "description": "Take out the trash from the kitchen",
        "completed": True,
        "created_at": "2021-09-01T12:00:00",
        "updated_at": "2021-09-01T12:00:00"
    }
]