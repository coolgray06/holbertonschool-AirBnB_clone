#!/usr/bin/python3

#BaseModel class inherent
from models.base_model import BaseModel as bm


class Amenity(bm):
    #class for our Amenity

    name = ""

    def __init__(self, *args, **kwargs):
        #initializing amenity
        super().__init__(*args, **kwargs)