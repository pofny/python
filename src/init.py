import json
import numpy as np
from src.classes.common import Character
from src.classes.human import Human
from src.classes.zombie import Zombie

def initialize():
    with open("../conf/human.json", "r") as f_human:
        loaded_json_human = json.load(f_human)

    with open("../conf/zombie.json", "r") as f_zombie:
        loaded_json_zombie = json.load(f_zombie)

    #print(np.random.normal(0, 10, 5))
    #print(loaded_json_human)
    #print(loaded_json_zombie)
    human_list = []
    zombie_list = []

    for i in range(loaded_json_human["initial_number"]):
        x = np.random.normal(*loaded_json_human["x"])
        y = np.random.normal(*loaded_json_human["y"])
        velocity = np.random.normal(*loaded_json_human["velocity"])
        power = np.random.normal(*loaded_json_human["power"])
        h = Human(x=x, y=y, velocity=velocity, power=power)
        human_list.append(h)

    for i in range(loaded_json_zombie["initial_number"]):
        x = np.random.normal(*loaded_json_zombie["x"])
        y = np.random.normal(*loaded_json_zombie["y"])
        velocity = np.random.normal(*loaded_json_zombie["velocity"])
        power = np.random.normal(*loaded_json_zombie["power"])
        z = Human(x=x, y=y, velocity=velocity, power=power)
        zombie_list.append(z)
        #print(zombie_list)

    return zombie_list, zombie_list

print(initialize())