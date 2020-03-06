import sys
import math
from datetime import date 
import random
import statistics as stat


print(math.cos(90))
print(sys.argv)
now = date.today()
print(now)
x = random.choice(["jambu",'apel','jeruk','durian'])
y = random.sample(range(100),10)
print(y)
print(x)
data =[10,11,14,45,34,13,15,56]
print(stat.mean(data))