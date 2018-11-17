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
from collections import deque

class MyAI ( Agent ):

    def __init__ ( self ):

        self.direction = 'right'
        self.currentPos = (1,1)
        self.hasArrow = True
        self.grabbed = False
        self.percepts = []
        self.explored = deque()
        self.makeUturn = False
        self.uTurnCount = 0


    def getAction( self, stench, breeze, glitter, bump, scream ):

        if (breeze or stench) and self.currentPos == (1,1):
            """
            if breeze:
                print("breeze")
            elif stench:
                print("stench")
            """
            #print("Run away")
            return Agent.Action.CLIMB
        else:
            if self.grabbed == True and self.currentPos == (1,1):
                return Agent.Action.CLIMB
            elif self.grabbed == True and self.currentPos != (1,1) and self.makeUturn == True and self.uTurnCount < 2:
                """
                    问题：在uturn的时候每个move都要回到这个function，第二次left的时候uturn条件已经没有了，uturn只run一次
                """
                self.uTurnCount+=1
                return self.uTurn()
            elif self.grabbed == True and self.currentPos != (1,1) and self.makeUturn == False:
                return self.goHome()
            if stench and self.hasArrow == False:
                "When percepts stench and you have no arrow. Escape"
                return
            elif glitter:
                self.grabbed = True
                return self.foundGold()
            elif bump:
                # if bump, turn until no bump
                self.explored.append(Agent.Action.TURN_LEFT)
                return self.turnLeft()
            else:
                self.explored.append(Agent.Action.FORWARD)
                return self.takeMove()

    def takeMove(self):
        if self.direction == 'right':
            self.currentPos = (self.currentPos[0]+1,self.currentPos[1])
        elif self.direction == 'left':
            self.currentPos = (self.currentPos[0]-1,self.currentPos[1])
        elif self.direction == 'up':
            self.currentPos = (self.currentPos[0],self.currentPos[1]+1)
        elif self.direction == 'down':
            self.currentPos = (self.currentPos[0],self.currentPos[1]-1)
        #print(self.currentPos)
        return Agent.Action.FORWARD


    def uTurn(self):
        actionL = [Agent.Action.TURN_LEFT,Agent.Action.TURN_LEFT]
        if self.direction == 'right':
            self.direction = 'up'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'down':
            self.direction = 'right'
        for a in actionL:
            return a

    def turnLeft(self):
        if self.direction == 'right':
            self.direction = 'up'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'down':
            self.direction = 'right'
        return Agent.Action.TURN_LEFT

    def turnRight(self):
        if self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'left':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'down':
            self.direction = 'left'
        return Agent.Action.TURN_RIGHT
    def shotArrow(self):
        self.hasArrow = False
        return Agent.Action.SHOOT

    def foundGold(self):
        self.grabbed = True
        self.makeUturn = True
        return Agent.Action.GRAB

    def goHome(self):
        self.uTurn()
        for move in range(len(self.explored)):
            nextMove = self.explored.pop()
            if nextMove == Agent.Action.TURN_LEFT:
                nextMove = Agent.Action.TURN_RIGHT
            elif nextMove == Agent.Action.TURN_RIGHT:
                nextMove = Agent.Action.TURN_LEFT
            return nextMove


            # if 0 < self.minimalCounter < 3:
            #     """
            #     Minimal AI
            #     When it moves one step ahead, turn around immediately
            #     """
            #     self.grabbed = True # Start going back
            #     #print("going back")
            #     self.minimalCounter = self.minimalCounter+1
            #     return self.uTurn()