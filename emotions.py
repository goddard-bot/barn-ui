import random
from collections import Counter
from driver import Robot_Driver


class Emotions:
    hap = random.randint(1, 100)
    hun = random.randint(1, 100)
    dis = random.randint(1, 100)
    sic = random.randint(1, 100)
    history = []
    boredom = 1

    def __init__(self, port='/dev/ttyUSB0'):
        port = Robot_Driver(port)

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
        if self.discipline_test():
            rest_mod = random.randint(1, 5)
            hun_val = -10 - rest_mod
            hap_val = 7 + rest_mod
            dis_val = -7 - rest_mod
            self.mod_hun(hun_val)
            self.mod_hap(hap_val)
            fri_val = self.mod_dis(dis_val)
            self.history.append("r")
            color = self.find_color(fri_val)
            self.port.sleep(color)
            return fri_val
        else:
            return self.mod_dis(0)

    def get_feed(self):
        if self.discipline_test():
            feed_mod = random.randint(1, 5)
            hun_val = 10 + feed_mod
            hap_val = 8 + feed_mod
            dis_val = -4 - feed_mod
            self.mod_hun(hun_val)
            self.mod_hap(hap_val)
            fri_val = self.mod_dis(dis_val)
            self.history.append("f")
            color = self.find_color(fri_val)
            self.port.yep(color)
            return fri_val
        else:
            return self.mod_dis(0)

    def get_play(self):
        if self.discipline_test():
            play_mod = random.randint(1, 5)
            hap_val = 10 + play_mod
            hun_val = -10 - play_mod
            self.mod_hap(hap_val)
            self.mod_hun(hun_val)
            fri_val = self.mod_hun(hun_val)
            self.history.append("p")
            color = self.find_color(fri_val)
            self.port.spin(color)
            return fri_val
        else:
            return self.mod_dis(0)

    def get_train(self):
        if self.discipline_test():
            train_mod = random.randint(1, 5)
            dis_val = 10 + train_mod
            hun_val = -7 - train_mod
            hap_val = -3 + train_mod
            self.mod_hap(hap_val)
            self.mod_hun(hun_val)
            fri_val = self.mod_dis(dis_val)
            self.history.append("t")
            color = self.find_color(fri_val)
            if random.randint(1, 2) == 1:
                self.port.go_forward(color, self.calc_obed_score()//10)
            else:
                self.port.reverse(color, self.calc_obed_score()//10)
            return fri_val
        else:
            return self.mod_dis(0)

    def get_heal(self):
        if self.discipline_test():
            heal_mod = random.randint(1, 5)
            sic_val = 10 + heal_mod
            dis_val = 5 + heal_mod
            hap_val = -3 - heal_mod
            self.mod_sic(sic_val)
            self.mod_dis(dis_val)
            fri_val = self.mod_hap(hap_val)
            self.history.append("h")
            color = self.find_color(fri_val)
            self.port.yep(color)
            return fri_val
        else:
            return self.mod_hun(0)

    def discipline_test(self):
        ran = random.randint(1, 100)
        if ran > self.calc_obed_score():
            color = self.find_color()
            self.port.get_mad(color)
            return False
        else:
            return True

    def find_color(self, fri_val):
        if self.hap > 50:
            greVal = self.hap//7
            redVal = 1
        else:
            redVal = (self.hap-50)//7
            greVal = 1
        blueVal = self.calc_obed_score()//7
        colorStr = str(int(redVal)) + str(int(greVal)) + str(int(blueVal))
        return colorStr
