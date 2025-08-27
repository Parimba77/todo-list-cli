# Utility functions for formatting and menu 

def line(msg): 
    print("-" * 30) 
    print(msg.center(30)) 
    print("-" * 30) 
    
def big_line(msg): 
        print("-" * 50) 
        print(msg.center(30)) 
        print("-" * 50) 
    
def menu(): 
    print("\033[34mChoose one of the options below:") 
    print() 
    print("\033[32m[ 1 ] \033[36mAdd Task") 
    print("\033[32m[ 2 ] \033[36mView Tasks") 
    print("\033[32m[ 3 ] \033[36mRemove Task") 
    print("\033[32m[ 4 ] \033[36mConcluir tarefa") 
    print("\033[32m[ 5 ] \033[36mExit") 
    print()