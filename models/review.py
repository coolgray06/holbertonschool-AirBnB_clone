#!/usr/bin/python3

#BaseModel class inherent
from models.base_model import BaseModel as bm


class Review(bm):
    #class for Review

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        #initialize Review

        super().__init__(*args, **kwargs)