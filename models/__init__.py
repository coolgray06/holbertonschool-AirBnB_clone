#!/usr/bin/python3

#makes a unique FileStorage instance for web app
from models.engine.file_storage import FileStorage

#variable storage, an instance for FileStorage
storage = FileStorage()
storage.reload()
