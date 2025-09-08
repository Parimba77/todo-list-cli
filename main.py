from utils.functions import *
from utils.colors import *
from db.crud import *
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
            try:
                print("Type the task you want to add:")
                task = input().strip()
                
                if not task:
                    raise ValueError("Task cannot be empty.")
                
            except KeyboardInterrupt:
                red()
                print("Task addition cancelled.")
                reset_format()
                sleep(0.5)
                
            except Exception as e:
                red()
                print(f"An error occurred: {e}")
                reset_format()
                sleep(0.5)
                    
            else:
                add_task(task)
                sleep(0.5)

        elif option == "2":
            try:
                print("Loading tasks...")
                sleep(1)
                
            except KeyboardInterrupt:
                KeyboardInterrupt_handler()
                
            except Exception as e:
                Exception_handler(e)
                
            else:
                view_tasks()



        elif option == "3":
            try:
                task_id = input("Type the ID of the task you want to remove: ").strip()
                if not task_id.isdigit():
                    raise ValueError("Please enter a valid task ID (number).")
            
            except KeyboardInterrupt:
                KeyboardInterrupt_handler()
                
            except Exception as e:
                Exception_handler(e)
            
            else:
                remove_task(int(task_id))



        elif option == "4":
            try:
                task_id = input("Type the ID of the task you want to mark as completed: ").strip()
                if not task_id.isdigit():
                    raise ValueError("Please enter a valid task ID (number).")
            
            except KeyboardInterrupt:
                KeyboardInterrupt_handler()
                
            except Exception as e:
                Exception_handler(e)
            
            else:
                complete_task(int(task_id))

        elif option == "5":
            print("See you soon!")
            break
        else:   # Invalid option
            red()
            print ("Error! Invalid Option.") 
            reset_format()