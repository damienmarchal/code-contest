"""
GET /nextCommand
    The response body must contain either NOTHING, UP, DOWN, OPEN or CLOSE
GET /call ?atFloor=[0-5]&to=[UP|DOWN]
GET /go ?floorToGo=[0-5]
GET /userHasEntered
GET /userHasExited
GET /reset ?cause=information+message
"""

class Ascenseur(object):
    def __init__(self, minEtage, maxEtage, initEtage):
        self.minEtage = minEtage
        self.maxEtage = maxEtage
        self.currentEtage = initEtage
        self.currentState = "NOTHING"

    def nextCommand(self):
        print("NextCommand")
        return "NOTHING"

    def call(self, atFloor : int, to : str):
        print("call")

    def go(self, floorToGo : int):
        print("go")    

    def userHasExited(self):
        print("userHasExited")    
    
    def userHasEntered(self):
        print("userHasEntered")    

    def reset(self, info):
        print("reset because of: info", info)    
        return "State is: " + str(self.currentEtage) + " " + str(self.currentState)  

import unittest
class TestAscenseur(unittest.TestCase):
    def test_nextCommand(self):
        a = Ascenseur(0, 5, 0)
        self.assertEqual(a.nextCommand(), "NOTHING")

if __name__ == '__main__':
    unittest.main()

