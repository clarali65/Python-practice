import timeit
import matplotlib.pyplot as plt
size = 101
list_res = []
dict_res = []
for i in range(size):
    test_list = [i for i in range(size)]
    t = timeit.Timer("del test_list[0]", "from __main__ import test_list")
    list_res.append(t.timeit(number=1))
for i in range(size):
    test_dict = {i: i for i in range(size)}
    t = timeit.Timer("del test_dict[%d]"%i, "from __main__ import test_dict")
    dict_res.append(t.timeit(number=1))
plt.figure()
plt.plot(range(size), list_res)
plt.plot(range(size), dict_res)
plt.legend(['del list', 'del dict'])
plt.show()