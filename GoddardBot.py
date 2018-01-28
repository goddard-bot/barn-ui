import random
from collections import Counter

class Emotions:
    hap = random.randint(1, 100)
    hun = random.randint(1, 100)
    dis = random.randint(1, 100)
    sic = random.randint(1, 100)
    history = []
    boredom = 1

    def calc_friend_score(self):
        sicChance = random.randint(1, 20)
        if sicChance == 1:
            self.sic += 10
        if len(self.history) > 20:
            self.history.pop()
        freqs = Counter(self.history)
        if max(freqs.values()) > 8:
            self.boredom = 0.5
            self.hap = self.hap / 2
            self.dis = self.dis * 2
        fri = ((self.hap * 4) - (self.hun * 0.5) + (self.dis * 0.5) - (self.sic * 0.5)) * self.boredom
        self.boredom = 1
        return fri

    def calc_obed_score(self):
        obed = 100 - self.dis
        return obed

    def mod_hap(self, hap):
        self.hap += hap
        if self.hap > 100:
            self.hap = 100
        elif self.hap < 0:
            self.hap = 0
        return self.calc_friend_score()

    def mod_hun(self, hun):
        self.hun += hun
        if self.hun > 100:
            self.hun = 100
        elif self.hun < 0:
            self.hun = 0
        return self.calc_friend_score()

    def mod_dis(self, dis):
        self.dis += dis
        if self.dis > 100:
            self.dis = 100
        elif self.dis < 0:
            self.dis = 0
        return self.calc_friend_score()

    def mod_sic(self, sic):
        self.sic += sic
        if self.sic > 100:
            self.sic = 100
        elif self.sic < 0:
            self.sic = 0
        return self.calc_friend_score()

    def get_rest(self):
        rest_mod = random.randint(1, 5)
        hun_val = -10 - rest_mod
        hap_val = 7 + rest_mod
        dis_val = -7 - rest_mod
        self.mod_hun(hun_val)
        self.mod_hap(hap_val)
        fri_val = self.mod_dis(dis_val)
        self.history.append("r")
        return fri_val

    def get_feed(self):
        feed_mod = random.randint(1, 5)
        hun_val = 10 + feed_mod
        hap_val = 8 + feed_mod
        dis_val = -4 - feed_mod
        self.mod_hun(hun_val)
        self.mod_hap(hap_val)
        fri_val = self.mod_dis(dis_val)
        self.history.append("f")
        return fri_val

    def get_play(self):
        play_mod = random.randint(1, 5)
        hap_val = 10 + play_mod
        hun_val = -10 - play_mod
        self.mod_hap(hap_val)
        self.mod_hun(hun_val)
        fri_val = self.mod_hun(hun_val)
        self.history.append("p")
        return fri_val

    def get_train(self):
        train_mod = random.randint(1, 5)
        dis_val = 10 + train_mod
        hun_val = -7 - train_mod
        hap_val = -3 + train_mod
        self.mod_hap(hap_val)
        self.mod_hun(hun_val)
        fri_val = self.mod_dis(dis_val)
        self.history.append("t")
        return fri_val

    def get_heal(self):
        heal_mod = random.randint(1, 5)
        sic_val = 10 + heal_mod
        dis_val = 5 + heal_mod
        hap_val = -3 - heal_mod
        self.mod_sic(sic_val)
        self.mod_dis(dis_val)
        fri_val = self.mod_hap(hap_val)
        self.history.append("h")
        return fri_val
