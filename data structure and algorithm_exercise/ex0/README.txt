1.做计时实验，验证list的按索引取值确实是O(1)

2.做计时实验，验证dict的get item和set item都是O(1)的

3.做计时实验，比较list和dict的del操作符性能

del lst[i]/del dic[key]

4.给定一个随机的数列表，验证list.sort的时间复杂度为O(nlogn) 

随机数列表样例：lst= [random.randrange(10**6) for n in range(10**4)]
