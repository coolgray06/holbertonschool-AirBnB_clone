#!/usr/bin/python3

import uuid
import datetime
import models

class base_model:
    #class for basemodel
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.name = name
        models.storage.new(self)


    def __str__(self):
        #string for basemodel instance
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
    

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        return self

    def to_dict(self):
        #returns a dictionary containing all keys/values
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.created_at.isoformat() 
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict 