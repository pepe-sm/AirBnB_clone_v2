#!/usr/bin/python3
"""This is a module that instantiates an object of class FileStorage"""
from os import getenv

"""this adds database and file storage"""
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
