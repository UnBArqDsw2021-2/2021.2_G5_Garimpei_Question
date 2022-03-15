from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from common.settings import (
    DATABASE_HOST, DATABASE_USER, DATABASE_PASS, DATABASE_DB, DATABASE_PORT
)


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
