import math
import random
from graphics import *

class Utils:
    def __init__(self):
        self = self
    
    def diff(self, x, y):
        return (y - x)
    def avg(self, x, y):
        return (x+y)/2

    def genGradient(self, redVals, greenVals, blueVals, dims, posx, posy):
        xp = posx/(dims-1)
        wg = ((dims-1)-posy)/(dims-1)
        rv1 = (redVals[0] + (self.diff(redVals[0], redVals[1])) * xp) * wg
        rv2 = (redVals[2] + (self.diff(redVals[2], redVals[3])) * xp) * (1-wg)
        gv1 = (greenVals[0] + (self.diff(greenVals[0], greenVals[1])) * xp) * wg
        gv2 = (greenVals[2] + (self.diff(greenVals[2], greenVals[3])) * xp) * (1-wg)
        bv1 = (blueVals[0] + (self.diff(blueVals[0], blueVals[1])) * xp) * wg
        bv2 = (blueVals[2] + (self.diff(blueVals[2], blueVals[3])) * xp) * (1-wg)
        finalRedVal = int(self.avg(rv1, rv2))
        finalGreenVal = int(self.avg(gv1, gv2))
        finalBlueVal = int(self.avg(bv1, bv2))
        color = '#%02X%02X%02X' % (finalRedVal, finalGreenVal, finalBlueVal)
        return color

    def listSwap(self, list, pos1, pos2):
     
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    def Shuffle(self, list, dims):
        corner = []
        newColors = []
        for a in range(4):
            corner.append((a%2)*(dims-1) + math.floor(a/2)*dims*(dims-1))
            save = list[corner[a]]
            newColors.append(save)
        del list[corner[3]]
        del list[corner[2]]
        del list[corner[1]]
        del list[corner[0]]
        random.shuffle(list)
        for a in range(4):
            insert = newColors[0]
            list.insert(corner[a], insert)
            del newColors [0]
        return corner

    def squareNumber(self, scale, point, dims):
        Os = []
        XP1 = math.floor(point.getX()/scale)
        YP1 = math.floor(point.getY()/scale)
        Os.append(YP1 * dims + XP1%dims)
        Os.append(Point(XP1 * scale, YP1 * scale))
        Os.append(Point((XP1+1) * scale, (YP1+1) * scale))
        return Os

        
    def highlightSquare(self, point1, point2, number, win):
        square = Rectangle(point1, point2)
        square.setOutline("red")
        square.setWidth(1)
        square.draw(win)

        

    def mValues (self, object):
        return object

