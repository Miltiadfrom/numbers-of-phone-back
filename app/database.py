from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///numbers.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
