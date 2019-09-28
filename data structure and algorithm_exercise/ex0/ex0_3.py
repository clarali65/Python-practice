import math
import random
import timeit
import matplotlib.pyplot as plt
res = []
for i in range(1000,100001,1000):
    lst = [random.randrange(10 ** 6) for n in range(i)]
    t = timeit.Timer("lst.sort()", "from __main__ import lst")
    res.append(t.timeit(number=100))
lg = []
for i in range(1000,100001,1000):
    lg.append(i*math.log(i,2))
fig,ax1 = plt.subplots()
ax1.scatter(range(1000,100001,1000), res)
ax2 = ax1.twinx()
ax2.plot(range(1000,100001,1000), lg)
fig.tight_layout()
plt.show()