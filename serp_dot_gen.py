from tkinter import *
from random import *
import time

def parse_dot(x, y, diameter=3):
    global canv
    d = diameter
    colors = ["black","green","red"]
    canv.create_oval(x-d/2,y-d/2,x+d/2,y+d/2, fill=colors[randint(0,2)])
    canv.update()

def gen_dot(dot1=[], dot2=[]):
    global dotlist
    if not dot1 and not dot2:
        dot1, dot2 = dotlist[randint(0, 2)], further_dotlist[randint(0, len(further_dotlist)-1)]
    x = (dot1[0] + dot2[0])/2
    y = (dot1[1] + dot2[1])/2
    further_dotlist.append([x,y])
    parse_dot(x, y)

def start_gen():
    for i in range(5000):
        gen_dot()


dotlist = [[256,8],[8,512],[512,512]]
further_dotlist = []

root = Tk()
canv = Canvas(root, width=525, height=525)
canv.pack()
but = Button(root, command=gen_dot, text="Generate a dot")
but.pack()

but_persist = Button(root, command=start_gen, text="Generate 1000")
but_persist.pack()


for i in dotlist: parse_dot(i[0],i[1])
gen_dot(dotlist[randint(0,2)], [randint(240, 300), randint(240, 300)])


root.mainloop()