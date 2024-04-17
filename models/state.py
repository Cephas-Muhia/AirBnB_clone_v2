#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()
        print(kwargs)
        """super().__init__(**kwargs)"""
        """self.name = kwargs["name"]"""
        if (kwargs["name"]):
            setattr(self, 'name', kwargs["name"])
