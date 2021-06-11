import math
import random

class Utils:
    def __init__(self):
        self = self
    
    def diff(self, x, y):
        return (y - x)
    def avg(self, x, y):
        return (x+y)/2
    
    def genGradient(self, xp, yp, scale, redVals, greenVals, blueVals, wg, posx, posy):
        finalRedVal = int(self.avg())
        finalGreenVal = int(self.avg((greenVals[0] + self.diff(greenVals[0], greenVals[1])*xp)*wg, (greenVals[2] + self.diff(greenVals[2], greenVals[3])*(1-wg))*wg))
        finalBlueVal = int(self.avg((blueVals[0] + self.diff(blueVals[0], blueVals[1])*xp)*wg, (blueVals[2] + self.diff(blueVals[2], blueVals[3])*(1-wg))*wg))
        color = '#%02X%02X%02X' % (finalRedVal, finalGreenVal, finalBlueVal)
        print("%s,%s,%s,%s,%s,%s" % (wg, xp, (1-wg), finalRedVal, finalGreenVal, finalBlueVal))
        return color
    
    
"""finalRedVal = int(redVals[0] + self.diff(redVals[0], redVals[1])*xp + self.diff(redVals[0], redVals[2])*yp)
        finalGreenVal = int(greenVals[0] + self.diff(greenVals[0], greenVals[1])*xp + self.diff(greenVals[0], greenVals[2])*yp)
        finalBlueVal = int(blueVals[0] + self.diff(blueVals[0], blueVals[1])*xp + self.diff(blueVals[0], blueVals[2])*yp)"""
