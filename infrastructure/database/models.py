from sqlalchemy import (
    # JSON,
    # Boolean,
    Column,
    # DateTime,
    # Float,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from .constants import (
    SQL_PATH
)


Base = declarative_base()


class ApiModel(Base):
    __tablename__ = "api_calls"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    firsname = Column(String)
    lastname = Column(String)
    phone = Column(Integer)
    website = Column(String)


engine = create_engine(
    SQL_PATH
)
Base.metadata.create_all(engine)
