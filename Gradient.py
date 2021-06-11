from graphics import *
import random
import keyboard
r = lambda: random.randint(0,255)
num4 = list(range(4))
sqrs = int(input("What are the dims you wish for:"))
sqs = list(range(sqrs))
sqsb = list(range(sqrs-1))
vals = []
vals.clear()
r1 = []
r2 = []
r3 = []
xd = 700
yd = 700
win = GraphWin("Game", xd, yd)
def diff(x, y) :
    return int(y - x)

def start() :
    for a in num4 : 
        r1.append(r())
        r2.append(r())
        r3.append(r())
        vals.append('#%02X%02X%02X' % (r1[a],r2[a],r3[a]))
        print (str(vals[a]))
        #print (str(r1[a]) + ", " + str(r2[a]) + ", " + str(r3[a]))

    for a in sqs :
        pt1 = Point(a * xd/sqrs, 0)
        pt2 = Point((a + 1) * xd/sqrs, yd/sqrs)
        #print (str(pt1) + ", " + str(pt2))
        rr1 = int(r1[0] + (diff(r1[0], r1[1]) * a/sqrs))
        rr2 = int(r2[0] + (diff(r2[0], r2[1]) * a/sqrs))
        rr3 = int(r3[0] + (diff(r3[0], r3[1]) * a/sqrs))
        color = '#%02X%02X%02X' % (rr1, rr2, rr3)
        #print (str(color) + ", " + str(rr1)+ ", " + str(rr2)+ ", " + str(rr3) )
        sq = Rectangle(pt1, pt2)
        sq.setFill(color)
        sq.draw(win) 
        i = a

        for a in sqsb :
            pt1 = Point(i * xd/sqrs, (a+1) * yd/sqrs)
            pt2 = Point((i + 1) * xd/sqrs, (a + 2) * yd/sqrs)
            bp1 = (r1[2] + (diff(r1[2], r1[3]) * i/sqrs))
            bp2 = (r2[2] + (diff(r2[2], r2[3]) * i/sqrs))
            bp3 = (r3[2] + (diff(r3[2], r3[3]) * i/sqrs))
            rr1 = int(rr1 + (diff(rr1, bp1) * a/sqrs))
            rr2 = int(rr2 + (diff(rr2, bp2) * a/sqrs))
            rr3 = int(rr3 + (diff(rr3, bp3) * a/sqrs))
            color = '#%02X%02X%02X' % (rr1, rr2, rr3)
            sq = Rectangle(pt1, pt2)
            sq.setFill(color)
            sq.draw(win)
        print (str(color))

start()
    

win.getMouse()
