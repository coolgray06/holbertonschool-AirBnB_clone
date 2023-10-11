#!/usr/bin/python3

#BaseModel class inherent
from models.base_model import BaseModel as bm

class State(bm):
    # class for State

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)