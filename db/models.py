from sqlalchemy import String, Integer, Column
from db.database import Base, db


# Task Model
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    def __init__(self, title, description=None):
        self.title = title
        self.description = description
        
    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', description='{self.description}')>"


# Creating Tables
Base.metadata.create_all(db)
