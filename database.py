from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config_credential = dotenv_values(".env")

POSTGRES_DATABASE_URL = f'''{config_credential["DB_CONNECTION"]}://{config_credential["DB_USERNAME"]}:{config_credential['DB_PASSWORD']}@{config_credential['DB_HOST']}:{config_credential['DB_PORT']}/{config_credential['DB_DATABASE']}'''

engine = create_engine(
    POSTGRES_DATABASE_URL
)


sessionLocal = sessionmaker(
    autoflush=False,autocommit = False,bind=engine
)

Base = declarative_base()

