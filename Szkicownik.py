
import numpy as np

k = []

for t in range(5):
    x = [t**2, t + 2]
    x1 = [t**2, t + 4]
    x2 = [t**2, t + 3]
    k.append([x, x1, x2])

for m in k:
    print m[0]
    print m[0][1]

