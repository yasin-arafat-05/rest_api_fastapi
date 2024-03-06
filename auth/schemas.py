from pydantic import BaseModel,Field



#__________________________ schemas for user ______________________

class User(BaseModel):
     email : str = Field(...,example="yasin@gmail.com")
     password : str = Field(...,example="123!@#$%")
     full_name : str = Field(...,example="Yasin Arafat")
     
     
