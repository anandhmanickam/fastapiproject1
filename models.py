from database import Base
from sqlalchemy import  Column,  Integer, String

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    age = Column(Integer)
    job = Column(String(30))
    email = Column(String(50), unique=True)
