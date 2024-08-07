import uuid
from datetime import datetime

def generate_id() -> str:
    return str(uuid.uuid4())

def get_current_date() -> str:
    return datetime.utcnow().isoformat()