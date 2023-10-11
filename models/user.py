
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