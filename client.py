#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
clients = {}


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openChatWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.configure(background="light blue")
    window.title('Music Window')
    window.geometry("420x410")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Select Song",bg="light blue", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    listbox = Listbox(window,height = 12,width = 50,activestyle = 'dotbox', bg="light blue", font = ("Calibri",10))
    listbox.place(x=35, y=40)

    play = Button(window,text="Play", width=12, bd=1,bg="light blue", font = ("Calibri",10))
    play.place(x=70,y=275)

    stop = Button(window,text="Stop", width=12, bd=1,bg="light blue",  font = ("Calibri",10))
    stop.place(x=265,y=275)

    upload = Button(window,text="Upload", width=12, bd=1,bg="light blue",  font = ("Calibri",10))
    upload.place(x=70,y=340)

    download = Button(window,text="Download", width=12, bd=1,bg="light blue",  font = ("Calibri",10))
    download.place(x=265,y=340)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()
