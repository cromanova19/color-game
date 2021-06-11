from graphics import *
from squares import Square
import math
import random
import keyboard
r = lambda: random.randint(0,255)
xd = 500
yd = 500
dims = 6
win = GraphWin("Game", xd, yd)
Corners = []
r1 = []
r2 = []
r3 = []
dimz = dims*2

def avg(x, y):
    return (x+y)/2

def diff(x, y):
    return (y - x)

for a in range (4):
    r1.append(r())
    r2.append(r())
    r3.append(r())

for a in range(dims**2):
    posx = a%dims
    posy = math.floor(a/dims)
    scale = xd/dims
    rr1 = int(r1[1] + diff(r1[1], r1[2])*posx/dimz + diff(r1[1], r1[3])*posy/dimz)
    rr2 = int(r2[1] + diff(r2[1], r2[2])*posx/dimz + diff(r2[1], r2[3])*posy/dimz)
    rr3 = int(r3[1] + diff(r3[1], r3[2])*posx/dimz + diff(r3[1], r3[3])*posy/dimz)
    color = '#%02X%02X%02X' % (rr1, rr2, rr3)
    Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
    Sq.generate()
    print (str(rr1) + ", " + str(rr2) + ", " + str(rr3))

for a in range (4):
    print (str(r1[a]))
    #print (str(r2[a]))
    #print (str(r3[a]))

win.getMouse()
