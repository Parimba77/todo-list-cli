from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import declarative_base, sessionmaker

# Creating Database Connection
db = create_engine('sqlite:///todo-list.db', echo=False)  
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()

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

# CRUD
def add_task(title, description=None):
    new_task = Task(title, description)
    session.add(new_task)
    session.commit()
    print(f"Task '{title}' added successfully!")
    print()

def view_tasks():
    tasks = session.query(Task).all()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✓" if task.description else "✗"
        print(f"[{status}] {task.id}: {task.title} - {task.description if task.description else 'No description'}")

def remove_task(task_id):
    task = session.get(Task, task_id)
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.title}' removed successfully!")
        print()
    else:
        print(f"No task found with ID {task_id}.")

def complete_task(task_id): 
    task = session.query(Task).filter(Task.id == task_id).first() 
    if task: 
        task.description = "Completed" 
        session.commit() 
        print(f"Task '{task.title}' marked as completed!") 
    else: 
        print(f"No task found with ID {task_id}.")