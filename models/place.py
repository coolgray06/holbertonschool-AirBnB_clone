#!/usr/bin/python3

#BaseModel class inherent
from models.base_model import BaseModel as bm


class Place(bm):
    #class for Place

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    max_guest = 0
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        #initializes Place
        super().__init__(*args, **kwargs)
