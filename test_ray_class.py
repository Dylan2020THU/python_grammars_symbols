"""
Goal: How to use ray architecture: class
Born time: 2022.5.16
Latest update: 2022.5.16
Creator: ZHX
"""

import ray
import time
import numpy as np


@ray.remote
class Counter():
    def __init__(self):
        print("Here")
        self.value = 0

    def incre(self):
        self.value += 1
        return self.value


c = Counter.remote()
id4 = c.incre.remote()
id5 = c.incre.remote()
print(ray.get([id4, id5]))
