"""
    Name: Anna Murphy
    Date: 27/1/2018
    File: RobotMain.py
"""

import friendship
import roboStats

class RobotMain:

    def __init__(self):
        friendshipVal = 0
        self.friendshipVal = friendship.Friendship().friendship

    def ask_mood(self):
        incVal = random.randint(1, 10)
        friendship.roboStats.updateHappiness(self, incVal)
        #Have the robit do something
    
def main():
    robitM = RobotMain()
    print(robitM.friendshipVal)

main()
