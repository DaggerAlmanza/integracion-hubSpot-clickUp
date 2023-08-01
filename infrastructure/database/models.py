from .constants import (
    SQL_PATH
)
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    JSON,
    String,
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ApiCallsModel(Base):
    __tablename__ = "api_calls"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    endpoint = Column(String)
    params = Column(JSON)
    result = Column(String)

    def to_json(self, *args, **kwargs):
        return {
            "id": self.id,
            "created_at": str(self.created_at),
            "endpoint": self.endpoint,
            "params": self.params,
            "result": self.result,
        }


engine = create_engine(
    SQL_PATH
)
Base.metadata.create_all(engine)
