import uuid # universally unique identifier
from datetime import datetime

def generate_id():
    return str(uuid.uuid4())

def get_current_date():
    return datetime.utcnow().isoformat()