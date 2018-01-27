from random import *
import time

def init_emots():
    hap = randint(1, 100)
    hun = randint(1, 100)
    dis = randint(1, 100)
    sic = 0
    return (hap, hun, dis, sic)

def cap_emots(hap, hun, dis, sic):
    if hap > 100:
        hap = 100
    elif hap < 0:
        hap = 0
    if hun > 100:
        hun = 100
    elif hun < 0:
        hun = 0
    if dis > 100:
        dis = 100
    elif dis < 0:
        dis = 0
    if sic > 100:
        sic = 100
    elif sic < 0:
        sic = 0
    return (hap, hun, dis, sic)

def calc_friend(hap, hun, dis, sic):
    if hun < 25:
        hunger = -(hun * 1.25)
    else:
        hunger = hun * 1.25
    friend = (hap * 4) + (hunger) - (dis * 0.5) - (sic * 0.5)
    friendVal = int(friend)
    return friendVal

def feed_robot(hap, hun):
    foodVal = randint(1, 20)
    hun += foodVal
    hap += (foodVal / 2)
    print("You fed the robot for", foodVal, "points!")
    print("Their happiness is now ", int(hap), " !", sep= "")
    print("")
    return (hap, hun)

def heal_robot(hap, dis, sic):
    medVal = randint(1, 30)
    sic -= medVal
    hap += (medVal / 4)
    dis -= (medVal / 4)
    print("You healed the robot for", medVal, "points!")
    print("Their sickness level is", sic, " now.")
    print("")
    return (hap, dis, sic)

def move():
    pass

def rest_robot(fri, hun, dis, sic):
    print("The robot is sleeping...")
    if fri > 100:
        hapVal = "very happy!"
    elif fri > 75:
        hapVal = "happy."
    elif fri > 50:
        hapVal = "ok."
    else:
        hapVal = "kinda sad."
    print("They are " + hapVal)
    if hun < 25:
        print("They are hungry...")
    else:
        print("They don't need food.")
    if sic > 0:
        print("And, they aren't feeling very well...")
    else:
        print("And, they're healthy!")
    

def play_robot():
    text_choose = randint(1,3)
    if text_choose == 1:
        print("The robot spun around!")
    elif text_choose == 2:
        print("The robot flashed their lights happily!")
    else:
        print("The robot did a thing.")#Later me please fix this
    return (text_choose * 5)

def main():
    happiness, hunger, discipline, sickness = init_emots()
    friendship = abs(calc_friend(happiness, hunger, discipline, sickness))
    while True:
        start = time.time()
        user_in = input("Interact with the Robot? ")
        if "feed" in user_in:
            happiness, hunger = feed_robot(happiness, hunger)
        elif "medicine" in user_in:
            happiness, discipline, sickness = heal_robot(happiness, discipline, sickness)
        elif "move" in user_in:
            move()
        elif "rest" in user_in:
            rest_robot(friendship, hunger, discipline, sickness)
            happiness += 5
        elif "play" in user_in:
            mod = play_robot()
            happiness += mod
            if mod%2 == 0:
                discipline += (mod/2)
        else:
            print("Invalid acttion. Valid actions include: ")
            print("Feed, give medicine, move, play with, and rest.")
            user_in_2 = input("Give another action? (enter to quit) ")
            if user_in_2 == "":
                break
            else:
                user_in = user_in_2
        hunger -= 10
        stop = time.time()
        dif = (stop - start)/2
        happiness -= int(dif)
        sickChance = randint(1, 100)
        if sickChance > 95:
            sickness += 5
        if sickness != 0:
            sickness += 10
        happiness, hunger, discipline, ickness = cap_emots(happiness,
                                                             hunger,
                                                             discipline,
                                                             sickness)
        friendship = calc_friend(happiness,
                                 hunger,
                                 discipline,
                                 sickness)


main()
