from tkinter import *
from tkinter import messagebox

tictactoe = Tk()

tictactoe.title("KrestikiNoliki")

Clicked = True
cout = 0


def Clicked():
   global count, winner

    # if button["text"] == " " and clicked == True:
    #     button["text"] = "X"
    #     Clicked = False
    #     count += 1


button1 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button1))
button2 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button2))
button3 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button3))

button4 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button4))
button5 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button5))
button6 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button6))

button7 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button7))
button8 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button8))
button9 = Button(tictactoe, bg='white', height=3, width=7, command=lambda: Clicked(button9))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

tictactoe.mainloop()