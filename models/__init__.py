#!/usr/bin/python3

"""Module for the init file"""

from models.engine.file_storage import FileStorage
""" After importing the file loads the objects from the file"""
storage = FileStorage()
storage.reload()
