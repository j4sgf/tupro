import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

data = pd.read_csv("Swarm016.tsp", delim_whitespace=True,
                   skipinitialspace=True)

sqrt = math.sqrt
x = data['X']
y = data['Y']
id = data['ID']
w, h = 16, 16
ec = [[0 for k in range(len(x))]for l in range(len(y))]
for i, dot1 in enumerate(id):
    a = np.array(x[i], y[i])
    for j, dot2 in enumerate(id):
        b = np.array(x[j], y[j])
        dist = np.linalg.norm(a - b)
        ec[i][j] = dist


np.savetxt('distance_matrix.txt', ec, fmt='%.2f')

fig, ax = plt.subplots()
plt.scatter(x, y, s=10, marker="2")

for i, txt in enumerate(id):
    ax.annotate(txt, (x[i], y[i]))
plt.show()
