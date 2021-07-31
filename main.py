import tkinter as Tk # Import our graphics module
from datetime import datetime # Lets us get current time and date
import sys # Get the system operating system
from threading import Thread # Get access to threading
from time import sleep # Useful for delaying time
import os # Gives us access to the CONSOLE
from zipfile import ZipFile # Unzip files!
from enum import Enum # for enum34, or the stdlib version

# --------
# Please enjoy using this code for your every purpose!
# It's completely free to fork it and make your own branch, so have fun!
# Best regards, Deltaion Lee
# --------

version = 0.1

root_path = os.path.abspath(os.sep)

project_root = os.path.dirname(os.path.abspath(__file__))

def kill(str:str = 'An internal process killed the running processes'):
    sys.exit(str)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def open_folder(str = "."):
    if OS == "mac":
        str = f"open {str}"
    elif OS == "windows":
        str = f"start {str}"
    else:
        return
    os.system(str)

t_OS = Enum('Operating System', 'windows mac ?')

OS = t_OS['?']
window_closed = True

if sys.platform.startswith("darwin"):
    OS = t_OS.mac
    app_path = project_root
elif sys.platform.startswith("win"):
    OS = t_OS.windows
    app_path = project_root
else:
    app_path = project_root

window = Tk.Tk()
window.title(f"Folder-Lock v{version}")
window.geometry("500x400+300+300")
window.resizable(False,False)

frame = Tk.Frame(window, width=800, height=400)
frame.pack()

timestamp = Tk.Label(frame,text=f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}",font=("Helvetica",12))
timestamp.place(x=350,y=5,width=150,height=20)

def time_loop():
    while True:
        timestamp.config(text=f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")
        sleep(1)

Thread(target=time_loop,args=(),daemon=True).start()

def unlock(key:str):
    ...

def call_unlock():
    ...

def lock(key:str):
    ...

def call_lock():
    ...

password_field = Tk.Text(frame,height=1,width=30)
password_field.insert("1.0", "Password")
password_field.place(x=145,y=50)

lock_button = Tk.Button(frame,text="Lock",font=("Helvetica",16),command=call_lock)
lock_button.place(x=175,y=100,width=150,height=20)

unlock_button = Tk.Button(frame,text="Unlock",font=("Helvetica",16),command=call_unlock)
unlock_button.place(x=175,y=150,width=150,height=20)

window_closed = False
window.mainloop()
window_closed = True
