from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import cfg


#SQLALCHEMY_DATABASE_URL = "sqlite:///./gspy/gl/encrypted_app.db" 
SQLALCHEMY_DATABASE_URL = "sqlite:///{0}".format(cfg['DB']['gl']) 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
