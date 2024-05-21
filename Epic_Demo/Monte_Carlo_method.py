"""
    園面積/矩形面積 = PI/4
    hits(落在圓內個數) = 1000000*pi/4
    pi = 4*hits/1000000
"""
import random

trials = 1000_000
hits = 0

for i in range(trials):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        hits += 1
PI = 4 * hits / trials
print("PI: ", PI)