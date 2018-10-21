import math

entropy = 0
p = [0.5, 0.5]
for i in p:
    entropy = entropy + (-i * math.log(i, 2))

print(entropy)
