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
        self.percepts = []
        self.explored = [(1,1)]
        self.minimalCounter = 0


    def getAction( self, stench, breeze, glitter, bump, scream ):

        if (breeze or stench) and self.currentPos == (1,1):
            """
            if breeze:
                print("breeze")
            elif stench:
                print("stench")
            """
            print("Run away")
            return Agent.Action.CLIMB
        else:
            if stench and self.hasArrow == False:
                "When percepts stench and you have no arrow. Escape"
                return
            elif glitter:
                self.grabbed = True
                return self.foundGold()
            if self.minimalCounter == 1:
                """
                Minimal AI
                When it moves one step ahead, turn around immediately 
                """
                self.grabbed = True # Start going back
                self.leftTurn()
                self.leftTurn()
                print("going back")
            if self.grabbed == True and self.currentPos == (0,0):
                return Agent.Action.CLIMB
            else:
                self.minimalCounter = self.minimalCounter + 1
                return self.takeMove()

    def takeMove(self):
        print("taking move")
        if self.direction == 'right':
            self.currentPos = (self.currentPos[0]+1,self.currentPos[1])
        elif self.direction == 'left':
            self.currentPos = (self.currentPos[0]-1,self.currentPos[1])
        elif self.direction == 'up':
            self.currentPos = (self.currentPos[0],self.currentPos[1]+1)
        elif self.direction == 'down':
            self.currentPos = (self.currentPos[0],self.currentPos[1]-1)
        print(self.currentPos)
        return Agent.Action.FORWARD


    def leftTurn(self):
        if self.direction == 'right':
            self.direction = 'up'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'down':
            self.direction = 'right'
        print("leftturn")
        return Agent.Action.TURN_LEFT

    def shotArrow(self):
        self.hasArrow = False
        return Agent.Action.SHOOT

    def foundGold(self):
        self.grabbed = True
        return Agent.Action.GRAB

