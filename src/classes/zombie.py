import numpy as np
from src.classes.common import Character


class Zombie(Character):
    def __init__(self, x, y, velocity, power, n_infected=0):
        super().__init__(x, y, velocity, power)
        self.n_infected = n_infected

    def __repr__(self):
        return f"Zombie (x={self.x}, y={self.y}, velocity={self.velocity}, " \
               f"power={self.power}, n_inf={self.n_inf})"

    def __str__(self):
        return "Zombie"

    def choose_new_position(self, humans):
        vectors_to_humans = [np.array([h.x - self.x, h.y - self.y]) for h in humans]
        vectors_to_humans_norm = [v / (np.linalg.norm(v) + 0.000001) for v in vectors_to_humans]
        weighted_vectors = [vn * (self.power + self.n_infected) - vn * (h.power + h.n_killed)
                            for vn, h in zip(vectors_to_humans_norm, humans)]
        sum_weighted_vectors = sum(weighted_vectors)
        normalized_vector_sum = (sum_weighted_vectors / (np.linalg.norm(sum_weighted_vectors) + 0.000001)) * self.velocity

        return normalized_vector_sum[0], normalized_vector_sum[1]