import os
import uuid

ID_FILE = "device_id.txt"

def get_device_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as f:
            return f.read().strip()

    new_id = str(uuid.uuid4())[:8]

    with open(ID_FILE, "w") as f:
        f.write(new_id)

    return new_id