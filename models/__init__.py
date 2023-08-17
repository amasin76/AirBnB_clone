#!/usr/bin/python3
"""auto __init__"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
