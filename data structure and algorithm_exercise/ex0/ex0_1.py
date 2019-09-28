from timeit import Timer
import random
import matplotlib.pyplot as plt
size = 1000
test_list = [i for i in range(size)]
test_dict = {i:i for i in range(size)}
res_list = []
read_dict = []

for i in range(size):
    t = timeit.Timer("test_list[%d]"%i, "from __main__ import test_list")
    res_list.append(t.timeit(number=1000))
for i in range(size):
    t = timeit.Timer("test_dict[%d]"%i, "from __main__ import test_dict")
    read_dict.append(t.timeit(number=1000))
write_dict = []
for i in range(size):
    t = timeit.Timer("test_dict[%d]=10"%i, "from __main__ import test_dict")
    write_dict.append(t.timeit(number=1000))
plt.figure()
plt.plot(test_list, res_list)
plt.plot(test_list, read_dict)
plt.plot(test_list, write_dict)
plt.legend(['list[i]', 'dict[i]', 'dict[i]=10'])
plt.show()