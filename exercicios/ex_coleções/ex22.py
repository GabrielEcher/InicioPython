

import random
from re import I

v1 = []
v2 = []
v3 = []

for n in range(10):
    v1.append(int(random.randint(0, 100)))
    v2.append(int(random.randint(0, 100)))

print(f"\nO valor do primeiro vetor é:\n{v1}")
print(f"\nO valor do segundo vetor é:\n{v2}")

for i in range((len(v1))):
    if i % 2 == 0:
        v3.append(v1[i])

for i in range((len(v2))):
    if i % 2 != 0:
        v3.append(v2[i])
        
print(f"\nO vetor final será {v3}")
