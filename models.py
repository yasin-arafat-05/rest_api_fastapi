from sqlalchemy import Column,Integer,text,String,Boolean
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "USER"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(100),nullable=False)
    password = Column(String(100),nullable= False)
    full_name = Column(String(50),nullable=False)
    create_on = Column(String(50),default=datetime.utcnow().date())
    status = Column(Boolean,default=False)
    