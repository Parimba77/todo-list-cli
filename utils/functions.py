# Utility functions for formatting and menu 
from time import sleep
from utils.colors import *

def line(msg): 
    print("-" * 30) 
    print(msg.center(30)) 
    print("-" * 30) 
    
def KeyboardInterrupt_handler(): 
    print() 
    red() 
    print("Operation cancelled by user.") 
    reset_format() 
    sleep(0.5) 
    
    
def Exception_handler(e): 
    red() 
    print(f"An error occurred: {e}") 
    reset_format() 
    sleep(0.5)

def menu(): 
    print("\033[34mChoose one of the options below:") 
    print() 
    print("\033[32m[ 1 ] \033[36mAdd Task") 
    print("\033[32m[ 2 ] \033[36mView Tasks") 
    print("\033[32m[ 3 ] \033[36mRemove Task") 
    print("\033[32m[ 4 ] \033[36mConcluir tarefa") 
    print("\033[32m[ 5 ] \033[36mExit") 
    print()