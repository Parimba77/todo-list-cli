from utils.functions import *
from utils.colors import *
from database import *
from time import sleep

if __name__ == "__main__":
    while True: 
        purple()
        line("To-Do List") 
        sleep(0.5)
        line("Main Menu")
        reset_format()
        
        bold()
        sleep(0.5)
        menu()

        option = input("Option: ") 
        print()

        if option == "1":
            print("Type the task you want to add:")
            task = input().strip()
            
            if task == "":
                red()
                print("Task cannot be empty!")
                reset_format()
                
            else:
                add_task(task)
            sleep(0.5)

        elif option == "2":
            view_tasks()

        elif option == "3":
            task_id = input("Type the ID of the task you want to remove: ").strip()
            if not task_id.isdigit():
                red()
                print("Please enter a valid task ID (number).")
                reset_format()
            else:
                remove_task(int(task_id))

        elif option == "4":
            task_id = input("Type the ID of the task you want to mark as completed: ").strip()
            if not task_id.isdigit():
                red()
                print("Please enter a valid task ID (number).")
                reset_format()
            else:
                complete_task(int(task_id))

        elif option == "5":
            print("See you soon!")
            break
        else:   # Invalid option
            red()
            print ("Error! Invalid Option.") 
            reset_format()