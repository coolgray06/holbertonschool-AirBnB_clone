#!/usr/bin/python3

#BaseModel class inherent
from models.base_model import BaseModel as bm


class City(bm):
    #the class for City
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        #initializing amenity
        super().__init__(*args, **kwargs)
        