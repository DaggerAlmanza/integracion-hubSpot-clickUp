from infrastructure.database.models import ApiCallsModel
from infrastructure.database.repository import Repository


class ApiCallsQuery(Repository):

    def __init__(self):
        super().__init__()
        self.conn = ApiCallsModel
