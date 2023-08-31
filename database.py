from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/app"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()