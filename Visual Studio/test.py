# Creating a simple register interface
from tkinter import *

def register():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Enter detatils below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    Entry(screen1, textvariable = username)
    Label(screen1, text="Password * ").pack()
    Entry(screen1, textvariable = password)


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Interface")
    Label(text="Interface", bg="grey", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()

main_screen()