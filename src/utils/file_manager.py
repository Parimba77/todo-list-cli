from src.utils import functions
from src.utils.colors import *
from time import sleep

def file_exists(file_name):
    try:
        f = open(file_name, "rt")
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def create_file(file_name):
    try:
        f = open(file_name, "wt+")
        f.close()
    except:
        print("Error while creating the file.")
    else:
        print(f"File {file_name} created successfully!")
        
        
def view_tasks(file_name):
    functions.line("Task List:")
    try:
        f = open(file_name, "rt")
    except:
        print("Error while trying to read the file.")
    else:   
        print(f.read())
        f.close()
        sleep(1)
        functions.line("End of Task List")
        
        
def add_task(file_name, task):
    try:
        f = open(file_name, "at")
    except:
        print("Error while opening the file.")
    else:
        try:
            f.write(f"{task}\n")
            f.close()
        except:
            print("Error while writing to the file.")
        else:
            print()
            print(f"Task ({task}) added successfully!")
            print()
            
def remove_task(file_name, task):
    try:
        f = open(file_name, "rt")
    except:
        print("Error while opening the file.")
    else:
        lines = f.readlines()
        f.close()
        
        if task + "\n" in lines:
            lines.remove(task + "\n")
            try:
                f = open(file_name, "wt")
                f.writelines(lines)
                f.close()
            except:
                print("Error while writing to the file.")
            else:
                print()
                print(f"Task '{task}' removed successfully!")
        else:
            print()
            print(f"Task '{task}' not found.")
        print()