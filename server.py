from tkinter import *

from tkinter import ttk

from vidstream import StreamingServer

import threading

import socket



import requests

import hashlib

import shutil



url = "https://raw.githubusercontent.com/AkisGeorg/sharescreen/master/server.py"



local_file_path = "server.py"



response = requests.get(url)

latest_version = response.text



latest_hash = hashlib.sha256(latest_version.encode()).hexdigest()



with open(local_file_path, "rb") as f:

    local_version = f.read()

local_hash = hashlib.sha256(local_version).hexdigest()



if latest_hash != local_hash:

    print("A new version of the script is available on GitHub. Updating...")

    with open(local_file_path, "w") as f:

        f.write(latest_version)

    print("Update successful!")

else:

    print("The script is up to date.")





# https://imgtr.ee/images/2023/05/01/JIhxY.png

class GUI:

    def __init__(self, master):

        self.master = master

        master.title("Share Screen Tool [Teacher]")

        master.geometry("350x200")

        master.configure(bg="#f2f2f2")

        master.resizable(False, False)

        p1 = PhotoImage()

        master.iconphoto(False, p1)

        self.connected_clients = []



        style = ttk.Style()

        style.theme_use("clam")

        style.configure("TLabel", background="#f2f2f2", foreground="#333", font=("Helvetica", 12))

        style.configure("TButton", background="#007bff", foreground="#fff", font=("Helvetica", 12), width=10)



        self.label1 = ttk.Label(master, text="Hostname: " + socket.gethostname())

        self.label1.pack(pady=5)



        self.label2 = ttk.Label(master, text="Session IP: " + socket.gethostbyname(socket.gethostname()))

        self.label2.pack(pady=5)



        self.start_button = ttk.Button(master, text="Start Sharing", name="start_button", command=self.start_server)

        self.start_button.pack(pady=10)



        self.close_button = ttk.Button(master, text="Stop Sharing", name="close_button", command=self.close,

                                       state=DISABLED)

        self.close_button.pack(pady=10)



        self.credits_label = ttk.Label(master, text="Credits: Akis Georgopoulos", font=("Helvetica", 8))

        self.credits_label.place(relx=1.0, rely=1.0, anchor=SE, in_=master, bordermode="outside")



    def start_server(self):

        self.server = StreamingServer(socket.gethostbyname(socket.gethostname()), 9999)

        self.thread = threading.Thread(target=self.server.start_server)

        self.thread.start()

        self.master.nametowidget("start_button").config(state=DISABLED)

        self.master.nametowidget("close_button").config(state=NORMAL)



    def close(self):

        self.server.stop_server()

        self.master.nametowidget("start_button").config(state=NORMAL)

        self.master.nametowidget("close_button").config(state=DISABLED)





root = Tk()

gui = GUI(root)

root.mainloop()

