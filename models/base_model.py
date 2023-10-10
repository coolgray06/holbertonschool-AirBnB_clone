import uuid
import datetime

class base_model:
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str



    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.name = name


    def __str__(self):
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
    


    def save(self):
        self.updated_at = datetime.datetime.now()

        return self
    
    def update_name(self, new_name):
        self.name = new_name
        
        
    
    def to_dict(self):
        print(self.__dict__)









class user:
    userID = str(uuid.uuid4())
    password: str
    name: str
    age: int

    def createUser(password, name, age):
        user.password = password
        user.name = name
        user.age = age
        return user




class house:
    address: set
    numBed: int
    numBath: int
    guests: user