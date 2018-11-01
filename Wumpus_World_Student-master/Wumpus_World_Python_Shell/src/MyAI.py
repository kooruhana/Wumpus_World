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


    def getAction( self, stench, breeze, glitter, bump, scream ):

        if (breeze or stench) and self.currentPos == (1,1):
            """
            if breeze:
                print("breeze")
            elif stench:
                print("stench")
            """
            return Agent.Action.CLIMB
        elif stench and self.hasArrow == False:
            "go back"
            return
        elif glitter:
            self.grabbed = True
            return self.foundGold()
        elif self.grabbed == True and self.currentPos == (0,0):
            return Agent.Action.CLIMB
        else:
            return Agent.Action.FORWARD

    def shotArrow(self):
        self.hasArrow = False
        return Agent.Action.SHOOT

    def foundGold(self):
        self.grabbed = True
        return Agent.Action.GRAB
    def 

