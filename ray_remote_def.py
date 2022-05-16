"""
Goal: How to use ray architecture: def
Born time: 2022.5.16
Latest update: 2022.5.16
Creator: ZHX
"""

import ray
import time
import numpy as np


@ray.remote  # ray.remote(read_array())
def read_array(file):
    print("read_array() is visited.", file)
    return file


@ray.remote
def add(a, b):
    print("add() is visited.")
    return np.add(a, b)


# the same functions (e.g. id1 and id2) below are executed in a parallel manner
id1 = read_array.remote(file=[1, 2, 3])
id2 = read_array.remote([4, 5, 6])
id3 = add.remote(id1, id2)  # this will be visited after id1 and id2
ray.get(id1)
ray.get(id2)
print(ray.get(id3))

