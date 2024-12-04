from os import path
from uuid import uuid4

def custom_upload_to(instance, filename, folder):
    ext = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{ext}'
    return path.join(folder, filename)
