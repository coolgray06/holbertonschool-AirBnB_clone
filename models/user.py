#!/usr/bin/python3

#the class user will inherent from BseModel
from models.base_model import BaseModel as bm

class User(bm):
    #class for User

    email = ""
    password = ""
    first_name = ""
    last_name = ""
