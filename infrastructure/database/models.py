from sqlalchemy import (
    JSON,
    # Boolean,
    Column,
    DateTime,
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
