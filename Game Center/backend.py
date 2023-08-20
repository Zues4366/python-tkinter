
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import random
from typing import List

play = True
clicked = True
count = 0
def click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
def spwindow():
    sp1_window= Toplevel()
    sp1_window.title("Tic-Tac-Toe")
    b1=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b1))
    b2=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b2))
    b3=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b3))

    b4=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b4))
    b5=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b5))
    b6=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b6))

    b7=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b7))
    b8=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b8))
    b9=Button(sp1_window, text=' ',font=BOLD,width=10, height=5, command= lambda:click(b9))


    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

def rpsclick(but):
    global clicked   
    computer = random.choice(['R', 'S', 'P'])
    if but["text"] != 'R' and but["text"] != 'P' and but["text"] != 'S':
        return messagebox.showinfo('Invalid Entry. Computer Selected %s'%(computer))
    elif but["text"] == computer:
        return messagebox.showinfo(message='It\'s a draw Computer Selected %s'%(computer))
    elif (but["text"] == 'R' and computer == 'S') or (but["text"] == 'S' and computer == 'P') or (but["text"] == 'P' and computer == 'R'):
        return messagebox.showinfo(message='You Win! Computer Selected %s'%(computer))
    else:
        return messagebox.showinfo(message='You Lose! Computer Selected %s'%(computer))

def rps():
    rps_win=Toplevel()
    rps_win.title("Rock-Paper-Scissors")

    but1 = Button(rps_win, text='R',font=BOLD,width=10, height=5, relief= RAISED, command= lambda:rpsclick(but1))
    but2 = Button(rps_win, text='P',font=BOLD,width=10, height=5,relief= RAISED, command= lambda:rpsclick(but2))
    but3 = Button(rps_win, text='S',font=BOLD,width=10, height=5,relief= RAISED, command= lambda:rpsclick(but3))
    but1.grid(row=1, column=0)
    but2.grid(row=1, column=1)
    but3.grid(row=1, column=2)

