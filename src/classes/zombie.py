class Zombie(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.n_infected = 0

    def choose_new_position(self, humans):
        delta_x = 2 * random.random() - 1
        delta_y = (1 - delta_x ** 2) ** 0.5 * (1 if random.random() > 0.5 else -1)

        delta_x *= self.velocity
        delta_y *= self.velocity

        return delta_x, delta_y