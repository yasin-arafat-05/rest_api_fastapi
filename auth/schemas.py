from pydantic import BaseModel



#__________________________ schemas for user ______________________

class User(BaseModel):
     email : str
     password : str
     full_name : str
     
     
