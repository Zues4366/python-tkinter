from tkinter import *
from tkinter.font import BOLD
import random
import backend

root=Tk()
root.geometry("500x500")
root.title("GAME CENTER")

def call_tic():
    backend.spwindow()

def call_rps():
    backend.rps()


main_frame=Frame(root)
Label(main_frame, text="Games", font=BOLD, fg='blue').grid(row=1, column=1)
Button(main_frame, text="Tic-Tac-Toe", command=(call_tic)).grid(row=2, column=1)
Button(main_frame, text="Rock-Paper-Scissors", command=(call_rps)).grid(row=3, column=1)
main_frame.pack()



root.mainloop()