from src.utils.functions import *
from src.utils.file_manager import *   # File handling functions
from src.utils.colors import *
from time import sleep

# Creating the file if it does not exist
file_name = "tasks.txt"
if not file_exists(file_name):
    create_file(file_name)

while True: 
    # Title and menu
    purple()
    line("To-Do List") 
    
    sleep(0.5)
    line("Main Menu")
    reset_format()
    
    bold()
    sleep(0.5)
    menu()
    
    # User options
    option = input("Option: ") 
    print()
    if option == "1":   # Add task
        print("Type the task you want to add:")
        add_task(file_name, input().strip())
        sleep(0.5)

    elif option == "2":   # View tasks
        sleep(0.5)
        view_tasks(file_name)

    elif option == "3":   # Remove task
        print("Type the task you want to remove:")
        remove_task(file_name, input().strip())

    elif option == "4":   # Exit
        print("See you soon!")
        break
    
    else:   # Invalid option
        red()
        unavailable()
        reset_format()