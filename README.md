# 📝 Todo List CLI

A simple **command-line task manager** built with Python, using **SQLAlchemy** with **SQLite**  
You can add, view, and remove tasks stored in a database.  

## 🚀 Features
- Add tasks
- View all tasks
- Remove tasks
- Persistent storage using SQLite database
- Colorful terminal output

## 🛠️ Technologies
- Python 3.10.12
- Standard Library (no external dependencies)
- SQLite (Database)
- SQLAlchemy (ORM)

## 📂 Project Structure

todo-list-cli/  
│── main.py  
│── database.py  
│── utils/  
│ ├── __init__.py  
│ ├── functions.py  
│ └── colors.py  
├── db/  
│   ├── __init__.py  
│   └── crud.py  
│   └── database.py  
│   └── models.py  
│── README.md  

## ▶️ How to Run

# Clone this repository
git clone https://github.com/Parimba77/todo-list-cli.git

# Navigate to the project folder
cd todo-list-cli/

# Install dependencies:

```bash
pip install -r requirements.txt
```

# Run the program
python main.py
