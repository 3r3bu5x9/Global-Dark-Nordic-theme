from tkinter import *
win = Tk()
topFrame = Frame(win)
topFrame.pack(side = TOP)
botFrame = Frame(win)
botFrame.pack(side = BOTTOM)

label1 = Label(topFrame,text = 'Lorem Ipsum',bg = 'pink')
label1.pack(side = LEFT)

button1 = Button(topFrame,text = 'press me',fg = 'red',bg = 'black')
button2 = Button(botFrame,text = 'press me',fg = 'cyan',bg = 'black')
button1.pack(side = LEFT)
button2.pack(side = RIGHT)

mainloop()
