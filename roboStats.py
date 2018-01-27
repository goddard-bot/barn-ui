"""
    Name: Anna Murphy
    File: roboStats.py
    Date: 27/1/2018

    This is the class for the
    robot emotional stats.
    Happiness, hunger, and
    discipline are the core ones.
    Additionally, there are sickness,
    and age. Sickness increses as a
    function of time infected,
    and age has specific incrememnts. 
    
"""

import random

class RoboStats:

    hunger = 0
    happiness = 0
    discipline = 0
    sickness = 0

    def __init__(self):        
        self.hunger = random.randint(0,100)
        self.happiness = random.randint(0, 100)
        self.discipline = random.randint(0, 100)

    def update_happiness(self, modify):
        self.happiness += modify
        if modify < 0:
            self.discipline -= (modify/2)
        else:
            self.discipline += (modify/2)

    def update_hungerFeed(self, food):
        self.hunger += food
        self.happiness += (food/2)

    def update_sickness(self, med):
        if self.sickness <= 0:
            self.discipline -= (med/2)
        self.sickness += med
        self.happiness += (med/4)

    def update_discipline(self):
        direction = random.randint(1, 2)
        amount = random.randint(1, 20)
        if direction == 1:
            self.discipline += amount
        else:
            self.discipline -= amount

