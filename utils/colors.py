# Module for color formatting in terminal output
def bold(): 
    print("\033[1m") 
    
def underline(): 
    print("\033[4m") 
    
def italic(): 
    print("\033[3m") 
    
def strike(): 
    print("\033[9m") 
    
def reset_format(): 
    print("\033[0m") 
    
def red(): 
    print("\033[1;31m") 
    
def green(): 
    print("\033[1;32m") 
    
def yellow(): 
    print("\033[1;33m") 
    
def blue(): 
    print("\033[1;34m") 
    
def purple(): 
    print("\033[1;35m") 
    
def cyan(): 
    print("\033[1;36m") 
    
def white(): 
    print("\033[1;37m") 
    
# Background colors
def bg_red(): 
    print("\033[41m") 
    
def bg_green(): 
    print("\033[42m") 
    
def bg_yellow(): 
    print("\033[43m") 
    
def bg_blue(): 
    print("\033[44m") 
    
def bg_purple(): 
    print("\033[45m") 
    
def bg_cyan(): 
    print("\033[46m") 
    
def bg_white(): 
    print("\033[47m")