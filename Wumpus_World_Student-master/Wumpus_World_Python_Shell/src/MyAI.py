# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent

class MyAI ( Agent ):

    def __init__ ( self ):

        self.direction = 'right'
        self.currentPos = (1,1)
        self.hasArrow = True
        self.grabbed = False
        self.explored = [(1,1)]


    def getAction( self, stench, breeze, glitter, bump, scream ):

        # --- STENCH NEAR WUMPUS --- #
        if stench and self.hasArrow == False:
            return
        if glitter:
            self.grabbed = True

        return Agent.Action.CLIMB

    def shotArrow(self):
        self.hasArrow = False
        return Agent.Action.SHOOT

    def turnLeft(self):
        if self.direction == "right":
            self.direction = "up"
        elif self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"

    def turnRight(self):
        if self.direction == "right":
            self.direction = "down"
        elif self.direction == "up":
            self.direction = "right"
        elif self.direction == "left":
            self.direction = "up"
        elif self.direction == "down":
            self.direction = "left"

    def uTurn(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "up":
            self.direction = "down"
        elif self.direction == "left":
            self.direction = "right"
        elif self.direction == "down":
            self.direction = "up"
