

class User:
    def __init__(self,userId,name,username,password,createdAt,updateAt,role):
        self.userId = userId
        self.name = name
        self.username = username
        self.password = password
        self.createdAt = createdAt
        self.updateAt = updateAt
        self.role = role