import numpy as np
from src.classes.common import Character

class Human(Character):
    def __init__(self, x, y, velocity, power, n_killed=0):
        super().__init__(x, y, velocity, power)
        self.n_killed = n_killed

    def __repr__(self):
        return f"Human (x={self.x}, y={self.y}, velocity={self.velocity}, " \
               f"power={self.power}, n_killed={self.n_killed})"

    def __str__(self):
        return "Human"

    def choose_new_position(self, zombies):
        vectors_to_zombies = [np.array([z.x - self.x, z.y - self.y]) for z in zombies]
        vectors_to_zombies_norm = [v / (np.linalg.norm(v) + 0.000001) for v in vectors_to_zombies]
        weighted_vectors = [vn * (self.power + self.n_killed) - vn * (z.power + z.n_infected)
                            for vn, z in zip(vectors_to_zombies_norm, zombies)]
        sum_weighted_vectors = sum(weighted_vectors)
        normalized_vector_sum = (sum_weighted_vectors / (np.linalg.norm(sum_weighted_vectors) + 0.000001)) * self.velocity

        return normalized_vector_sum[0], normalized_vector_sum[1]