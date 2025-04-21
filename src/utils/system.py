import os
import platform

def clear_screen():
    """
    Clears the console screen.
    Works on Windows, Mac, and Linux.
    """
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")