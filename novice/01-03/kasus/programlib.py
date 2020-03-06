import statistics as stat
import random
import numpy as np

BB = random.sample(range(50,100),45)
print('data = ',BB)
print(stat.mean(BB))
print(stat.median(BB))
print(stat.stdev(BB))
print(np.average(BB))
