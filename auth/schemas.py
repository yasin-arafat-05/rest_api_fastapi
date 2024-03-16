from pydantic import BaseModel,Field



#__________________________ schemas for user ______________________

class User(BaseModel):
     email : str = Field(...,example="yasin@gmail.com")
     password : str = Field(...,example="123!@#$%")
     full_name : str = Field(...,example="Yasin Arafat")
     
     
class ResetPassword(BaseModel):
     old_password : str = Field(...,example="Old Password")
     new_password : str  = Field(...,example="New Password")
     confirm_password : str = Field(...,example="Confirm Password")
     
class ChangePassword(BaseModel):
     old_password : str 
