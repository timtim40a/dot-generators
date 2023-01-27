from tkinter import *
from random import *
import time

def parse_dot(x, y):
    global canv
    canv.create_oval(x-1,y-1,x+1,y+1)
    canv.update()

def gen_dot():
    global dotlist
    dot1, dot2 = randint(0, len(dotlist)-1), randint(0, len(dotlist)-1)
    while dot2 == dot1:
        dot2 = randint(0, len(dotlist)-1)
    x = (dotlist[dot1][0] + dotlist[dot2][0])/2
    y = (dotlist[dot1][1] + dotlist[dot2][1])/2
    dotlist.append([x,y])
    parse_dot(x, y)

def start_gen():
    for i in range(5000):
        gen_dot()


dotlist = [[256,8],[8,512],[512,512]]

root = Tk()
canv = Canvas(root, width=525, height=525)
canv.pack()
but = Button(root, command=gen_dot, text="Generate a dot")
but.pack()

but_persist = Button(root, command=start_gen, text="Generate 1000")
but_persist.pack()


for i in dotlist: parse_dot(i[0],i[1])

root.mainloop()