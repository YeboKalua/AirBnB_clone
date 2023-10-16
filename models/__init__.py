#!/usr/bin/python3
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

__all__ = ["user", "base_model", "state", "city", "amenity", "place", "review"]
