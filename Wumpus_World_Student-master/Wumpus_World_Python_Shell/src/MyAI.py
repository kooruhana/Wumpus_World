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

"""
    一直forward 碰见gold就捡，碰见任何breeze或者stench都直接掉头
"""

from Agent import Agent
from collections import deque

class MyAI ( Agent ):

    def __init__ ( self ):

        self.direction = 'right'
        self.currentPos = (1,1)
        self.hasArrow = True
        self.grabbed = False
        self.nextMove = deque()
        self.explored = deque()
        self.makeUturn = False
        self.back = False
        self.oneMore = False # hard code
        self.uTurnCount = 0 # 因为uTurn要左转两次，用来作为判断条件（Count<2）
        self.ForceuTurnCount = 0 # hard code


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
            # print(self.currentPos)
            if glitter:
                self.grabbed = True
                return self.foundGold()
            if self.back and self.currentPos == (1,1):
                return Agent.Action.CLIMB

            # if self.oneMore == True:
            #     self.oneMore = False
            #     self.nextMove.append(Agent.Action.TURN_LEFT)
            #     return self.takeMove(self.nextMove.pop())

            if self.grabbed == True and self.makeUturn == True:
                self.uTurnCount+=1
                self.back = True
                if self.uTurnCount <= 2:
                    self.explored.append(Agent.Action.TURN_LEFT)
                return self.takeMove(self.explored.pop())

            if bump and self.grabbed == False and self.makeUturn == False:
                # if bump, turn until no bump
                #self.explored.append(Agent.Action.TURN_LEFT)
                if self.ForceuTurnCount == 0:
                    self.explored.append([Agent.Action.TURN_LEFT])
                    self.nextMove.extend([Agent.Action.TURN_LEFT])

                print(self.explored)
                # self.oneMore = True
                return self.takeMove(self.nextMove.pop())

            if stench and self.grabbed == False and self.makeUturn == False and self.ForceuTurnCount < 2:
                if self.ForceuTurnCount == 0:
                    self.explored.extend([Agent.Action.TURN_LEFT,Agent.Action.TURN_LEFT])
                    self.nextMove.extend([Agent.Action.TURN_LEFT,Agent.Action.TURN_LEFT])
                self.ForceuTurnCount += 1
                self.back = True
                return self.takeMove(self.nextMove.pop())

            if breeze and self.grabbed == False and self.makeUturn == False and self.ForceuTurnCount < 2:
                if self.ForceuTurnCount == 0:
                    self.explored.extend([Agent.Action.TURN_LEFT,Agent.Action.TURN_LEFT])
                    self.nextMove.extend([Agent.Action.TURN_LEFT,Agent.Action.TURN_LEFT])
                self.ForceuTurnCount += 1
                self.back = True
                return self.takeMove(self.nextMove.pop())

            self.explored.append(Agent.Action.FORWARD)
            self.nextMove.append(Agent.Action.FORWARD)
            return self.takeMove(self.nextMove.pop())

    def takeMove(self,move):
        # qprint("direction: "+self.direction)
        if self.back == True:
            for move in range(len(self.explored)):
                next_move = self.explored.pop()
                if next_move == Agent.Action.TURN_LEFT:
                    next_move = Agent.Action.TURN_RIGHT
                elif next_move == Agent.Action.TURN_RIGHT:
                    next_move = Agent.Action.TURN_LEFT
                return next_move
        if move == Agent.Action.FORWARD:
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

        elif move in [Agent.Action.TURN_LEFT,Agent.Action.TURN_RIGHT]:
            if move == Agent.Action.TURN_LEFT:
                if self.direction == 'right':
                    self.direction = 'up'
                elif self.direction == 'left':
                    self.direction = 'down'
                elif self.direction == 'up':
                    self.direction = 'left'
                elif self.direction == 'down':
                    self.direction = 'right'
                return Agent.Action.TURN_LEFT
            else:
                if self.direction == 'right':
                    self.direction = 'down'
                elif self.direction == 'left':
                    self.direction = 'up'
                elif self.direction == 'up':
                    self.direction = 'right'
                elif self.direction == 'down':
                    self.direction = 'left'
                return Agent.Action.TURN_RIGHT


    # def uTurn(self):
    #     actionL = [Agent.Action.TURN_LEFT,Agent.Action.TURN_LEFT]

    def shotArrow(self):
        self.hasArrow = False
        return Agent.Action.SHOOT

    def foundGold(self):
        self.grabbed = True
        self.makeUturn = True
        return Agent.Action.GRAB



            # if 0 < self.minimalCounter < 3:
            #     """
            #     Minimal AI
            #     When it moves one step ahead, turn around immediately
            #     """
            #     self.grabbed = True # Start going back
            #     #print("going back")
            #     self.minimalCounter = self.minimalCounter+1
            #     return self.uTurn()