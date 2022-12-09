class Character:
    def __init__(self, **kwarks):
        self.x = kwarks["x"]
        self.y = kwarks["y"]
        self.velocity = kwarks["velocity"]
        self.power = kwarks["power"]

    def move(self, delta_x, delta_y):
        self.x = x + delta_x
        self.y = y + delta_y