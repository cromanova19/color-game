from graphics import *
import random
import keyboard
r = lambda: random.randint(0,255)

class Square :
    def __init__(self, P1, P2, color, win):
        self.P1 = P1
        self.P2 = P2
        self.color = color
        self.win = win

    def generate(self):
        sqs = Rectangle(self.P1, self.P2)
        sqs.setFill(self.color)
        sqs.draw(self.win)

    """def shuffle(self):
        sqs = Rectangle(self.P1, self.P2)
        sqs.setFill(self.color)
        sqs.draw(self.win)"""

    

