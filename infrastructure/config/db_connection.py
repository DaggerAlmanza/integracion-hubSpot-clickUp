from sqlalchemy.orm import sessionmaker
from infrastructure.database.models import engine


Session = sessionmaker(bind=engine)
session = Session()
