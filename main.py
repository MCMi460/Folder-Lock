import tkinter as Tk # Import our graphics module
from datetime import datetime # Lets us get current time and date
import sys # Get the system operating system
from threading import Thread # Get access to threading
from time import sleep # Useful for delaying time
import os # Gives us access to the CONSOLE
from zipfile import ZipFile # Unzip and zip files!
from enum import Enum # To make Enums in Python!
import urllib.parse # An amazing way to make URL-Safe strings!
from utility import File, Timer # My utilities I wrote on vacation!

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

def checkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def open_folder(str = "."):
    if OS == t_OS.mac:
        str = f"open {str}"
    elif OS == t_OS.windows:
        str = f"start {str}"
    else:
        return
    os.system(str)

t_OS = Enum('Operating System', 'windows mac ?')

OS = t_OS['?']
window_closed = True
processing = False
username = "Superuser"

separator = "||__||"

if sys.platform.startswith("darwin"):
    OS = t_OS.mac
    app_path = project_root
    username = os.getlogin()
elif sys.platform.startswith("win"):
    OS = t_OS.windows
    app_path = project_root
    username = os.getlogin()
else:
    app_path = project_root
archive_path = f"{project_root}/STORAGE"

checkdir(f"ARCHIVE/")
checkdir(f"STORAGE/")

window = Tk.Tk()
window.title(f"Folder-Lock v{version}")
window.geometry("500x400+300+300")
window.resizable(False,False)

frame = Tk.Frame(window, width=800, height=400)
frame.pack()

author = Tk.Label(frame,text="By Deltaion Lee!")
author.config(font=("Helvetica",12))
author.place(x=190,y=5,width=120,height=20)
author.bind("<Button-1>", lambda e: open_folder("https://github.com/MCMi460"))

user = Tk.Label(frame,text=username,anchor='w')
user.config(font=("Helvetica",12))
user.place(x=0,y=5,width=120,height=20)
user.bind("<Button-1>", lambda e: open_folder(f"https://ghostr.mi460.dev/user/search?user={urllib.parse.quote(username)}"))

timestamp = Tk.Label(frame,text=f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}",font=("Helvetica",12))
timestamp.place(x=350,y=5,width=150,height=20)

def time_loop():
    while True:
        timestamp.config(text=f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}")
        sleep(1)

Thread(target=time_loop,args=(),daemon=True).start()

def encrypt(key, bytes_list):
    encoded_items = []
    bytes_list = [b'%c' % i for i in bytes_list]
    for i in range(len(bytes_list)):
        key_c = key[i % len(key)]
        encoded_c = (int.from_bytes(bytes_list[i], sys.byteorder) + ord(key_c)) % 512
        encoded_items.append(str(encoded_c) + separator)
    return encoded_items

def decrypt(key, bytes_list):
    encoded_items = []
    temp = bytes_list.split(separator)
    bytes_list = []
    for i in temp:
        try:
            bytes_list.append(int(i))
        except:
            pass
    for i in range(len(bytes_list)):
        key_c = key[i % len(key)]
        encoded_c = (bytes_list[i] - ord(key_c) + 512) % 512
        encoded_items.append(encoded_c.to_bytes(1, sys.byteorder))
    return encoded_items

def unlock(key:str):
    global processing
    processing = True
    print("Encoding passkey...")
    notice.config(text="Encoding passkey...")
    key = urllib.parse.quote(key)
    print(f"\nLock (key:str): [\nRegister password using `{key}`\n(Decoded as {urllib.parse.unquote(key)})\n]\n")
    sleep(0.1)
    print("Getting file data...")
    notice.config(text="Getting file data...")
    files = [f for f in os.listdir(archive_path) if os.path.isfile(os.path.join(archive_path, f))]
    sleep(0.1)
    try: files.remove('.DS_Store')
    except: pass
    files_n = len(files)
    count = 0
    sleep(0.1)
    for item in files:
        count += 1
        print(f"Rewriting files... {count}/{files_n}")
        notice.config(text=f"Rewriting files...{count}/{files_n}")

        file = File(f"{archive_path}/{item}")

        try:
            data_buffer = file.read()
            if not "_*" in data_buffer:
                continue
        except:
            continue

        try:
            decrypted = decrypt(key, data_buffer.lstrip("_*"))
            file.write_bytes(b''.join(decrypted))
        except:
            print(f"Error on file {count}/{files_n}\nFile name: {item}")
            notice.config(text=f"Error on file {count}/{files_n}")
            sleep(1)
            print(f"Proceeding with restoring backup...")
            notice.config(text=f"Proceeding with restoring backup...")
            archives = [f for f in os.listdir(f"{archive_path.replace('/STORAGE','')}/ARCHIVE") if os.path.isfile(os.path.join(f"{archive_path.replace('/STORAGE','')}/ARCHIVE", f))]
            try:
                archives.remove('.folder-lock')
                archives.remove('.DS_Store')
            except: pass
            date_time_obj = datetime.strptime("1970-01-01|00-00", '%Y-%m-%d|%H-%M')
            zip = None
            for archive in archives:
                try:
                    if datetime.strptime(archive.replace(".zip",""), '%Y-%m-%d|%H-%M') > date_time_obj:
                        date_time_obj = datetime.strptime(archive.replace(".zip",""), '%Y-%m-%d|%H-%M')
                        zip = archive
                    print(f"{archive}...")
                except:
                    pass
            sleep(0.2)
            print(f"Found archive {zip}...")
            notice.config(text=f"Found archive {zip}...")
            sleep(0.1)
            try:
                with ZipFile(f"ARCHIVE/{zip}", 'r') as zip_ref:
                    zip_ref.extractall(f"{archive_path}")
                print(f"Extracted {zip} successfully!")
                notice.config(text=f"Extracted {zip} successfully!")
                print(f"Warning, the extracted file may not be exactly perfect. Please check the directory before use.")
            except:
                print(f"Could not extract {zip}.")
                notice.config(text=f"Could not extract {zip}.")
            sleep(0.1)
            processing = False
            return

        sleep(0.1)
    print(f"Successfully decrypted files!")
    notice.config(text=f"Successfully decrypted files!")
    processing = False

def call_unlock():
    if not processing:
        Thread(target=unlock,args=(password_field.get("1.0",'end-1c'),),daemon=False).start()

def lock(key:str):
    global processing
    processing = True
    print("Encoding passkey...")
    notice.config(text="Encoding passkey...")
    key = urllib.parse.quote(key)
    print(f"\nLock (key:str): [\nRegister password using `{key}`\n(Decoded as {urllib.parse.unquote(key)})\n]\n")
    sleep(0.1)
    print("Getting file data...")
    notice.config(text="Getting file data...")
    files = [f for f in os.listdir(archive_path) if os.path.isfile(os.path.join(archive_path, f))]
    sleep(0.1)
    try: files.remove('.DS_Store')
    except: pass
    files_n = len(files)
    count = 0
    sleep(0.1)
    locked = True
    for file in files:
        count += 1
        print(f"Rewriting files... {count}/{files_n}")
        notice.config(text=f"Rewriting files...{count}/{files_n}")

        file = File(f"{archive_path}/{file}")

        data_buffer = file.read_bytes()
        try:
            if "_*" in file.read():
                continue
        except:
            pass

        try:
            encrypted = encrypt(key, data_buffer)
            file.overwrite("_*" + ''.join(encrypted))
            locked = False
        except:
            print(f"Error on file {count}/{files_n}\nFile: {file}")
            notice.config(text=f"Error on file {count}/{files_n}")
            sleep(1)
            processing = False
            return

        sleep(0.1)
    if not locked:
        print(f"Archiving files...")
        notice.config(text=f"Archiving files...")
        filename = f"ARCHIVE/{datetime.now().strftime('%Y-%m-%d|%H-%M')}.zip"
        zipObj = ZipFile(filename, 'w')
        for file in files:
            zipObj.write(f"{archive_path}/{file}")
        zipObj.close()
        sleep(0.1)
    print(f"Successfully encrypted files!")
    notice.config(text=f"Successfully encrypted files!")
    processing = False

def call_lock():
    if not processing:
        Thread(target=lock,args=(password_field.get("1.0",'end-1c'),),daemon=False).start()

password_field = Tk.Text(frame,height=1,width=30)
password_field.insert("1.0", "Password")
password_field.place(x=145,y=50)

lock_button = Tk.Button(frame,text="Lock",font=("Helvetica",16),command=call_lock)
lock_button.place(x=175,y=100,width=150,height=20)

unlock_button = Tk.Button(frame,text="Unlock",font=("Helvetica",16),command=call_unlock)
unlock_button.place(x=175,y=150,width=150,height=20)

notice = Tk.Label(frame,text="All data to be stored must be in a folder named \"STORAGE\"")
notice.config(font=("Helvetica",14))
notice.place(x=0,y=350,width=500,height=30)
notice.bind("<Button-1>", lambda e: open_folder("STORAGE"))

window_closed = False
window.mainloop()
window_closed = True
