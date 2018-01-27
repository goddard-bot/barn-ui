"""
rowan d'ausilio
friendship.py

friendship start at a calculated value from all the other stats
formula how think it could be
"""

import roboStats


class Friendship:
    """A class to represent the friendship level of the robot"""

    def __init__(self):
        """initialize the friendship level of the robot"""
        self.friendship = 0
        stats = roboStats
        self.init_friendship = 0
        self.base_friendship(stats)

    def base_friendship(self, stats):
        self.friendship = stats.RoboStats.discipline + stats.RoboStats.happiness + stats.RoboStats.hunger
        self.init_friendship = self.friendship

    def update_friendship(self, stats):
        happiness = stats.RoboStats.happiness  # plus
        hunger = stats.RoboStats.hunger
        discipline = stats.RoboStats.discipline  # minus
        sickness = stats.RoboStats.sickness  # minus if above 0

        if hunger < 25:
            new_hunger = -(hunger * 1.25)
        else:
            new_hunger = hunger * 1.25

        friendship_level = (happiness * 4) - (discipline * 0.5) + new_hunger - (sickness * 0.5)
