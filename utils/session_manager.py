import random

# HashMap storing active devices
active_devices = {}

def generate_device_id():
    return str(random.randint(100000,999999))

def register_device(device_socket):
    device_id = generate_device_id()
    active_devices[device_id] = device_socket
    return device_id

def get_device(device_id):
    return active_devices.get(device_id)