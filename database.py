from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base



POSTGRES_DATABASE_URL = "postgresql://user:password@postgresserver/db"
Base = declarative_base()