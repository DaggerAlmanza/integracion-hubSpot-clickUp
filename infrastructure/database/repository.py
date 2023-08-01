from infrastructure.config.db_connection import session
from infrastructure.database.models import Base


class Repository():

    def __init__(self):
        self.session = session
        self.conn = Base

    def get_query(self):
        data = self.session.query(self.conn).all()
        return data

    def create_query(self, data: dict) -> bool:
        try:
            see = self.conn(
                **data
                )
            self.session.add(see)
            self.session.commit()
            self.session.close()
            return True
        except Exception as error:
            print(error)
            return False
