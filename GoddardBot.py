import random

class Emotions:
    hap = random.randint(1, 100)
    hun = random.randint(1, 100)
    dis = random.randint(1, 100)
    sic = random.randint(1, 100)

    def calc_friend_score(self):
        fri = (self.hap * 4) - (self.hun * 0.5) + (self.dis * 0.5) - (self.sic * 0.5)
        return fri

    def calc_obed_score(self):
        obed = 100 - self.dis
        return obed

    def mod_hap(self, hap):
        self.hap += hap
        return self.calc_friend_score()

    def mod_hun(self, hun):
        self.hun += hun
        return self.calc_friend_score()

    def mod_dis(self, dis):
        self.dis += dis
        return self.calc_friend_score()

    def mod_sic(self, sic):
        self.sic += sic
        return self.calc_friend_score()
