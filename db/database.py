from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import declarative_base, sessionmaker

# Creating Database Connection
db = create_engine('sqlite:///todo-list.db', echo=False)  
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()
