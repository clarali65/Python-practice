1字符串中所有重排（10分）
题目内容：

给定一个字符串s与待查找字符串p，请给出使得s[i:i+len(p)]是p的一个字母重排的所有下标i

题目保证字符串p非空



输入格式:

两行字符串，第一行为s，第二行为p



输出格式：

所有满足条件的下标从小到大排列，以空格分隔输出

若无对应下标，则输出"none"



输入样例：

cbaebabacd

abc



输出样例：

0 6



参考代码模板：

def findAnagrams(s, p):
    # code here
    pass
 
s = input()
p = input()
findAnagrams(s, p)




2列表出现最频繁的元素（10分）
题目内容：

给定一个列表与数字K，按出现次数倒序输出列表中前K个出现最频繁的元素；若少于K个元素则返回所有元素



输入格式:

输入为两行

第一行为给定列表，以合法的Python表达式给出

第二行为数字K



输出格式：

不多于K个数字，以空格分隔



输入样例：

[1,1,1,2,2,3]

2



输出样例：

1 2



参考代码模板：

def topKFrequent(nums, k):
    # code here
    pass
 
lst = eval(input())
k = int(input())
topKFrequent(lst, k)





3散列表（10分）
题目内容：

给定一个指定大小N的散列表，并输入一系列数字：若找到空槽，则插入该数字，并返回槽位置；若该数字在散列表中存在，则直接输出其位置。

注：使用下标增加的二次探测法解决散列冲突

注2：散列表实际大小应确定为不小于用户输入N的最小质数



输入格式:

两行

第一行为用户指定散列表大小N

第二行为一系列数字，以空格分隔



输出格式：

逐个输出对应数字在散列表中位置，以空格分隔

若该数字无法插入，则输出“-”



输入样例：

4

10 6 4 10 15



输出样例：

0 1 4 0 -



参考代码模板：

def createHashTable(n):
    # code here
    pass
 
def insertNumbers(table, nums):
    # code here
    pass
 
n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)