#!/usr/bin/python3
"""
This module contains the User class that inherits from BaseModel.
"""

from models.base_model import BaseModel  # Import BaseModel


class User(BaseModel):
    """User class inheriting from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
