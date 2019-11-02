# fast sort algorithm
def fastsort(list):
    MainUnit = 0
    MainUnitList = []
    l = len(list)
    for idx in range(l):
        leftok = False
        if idx == 0:#第一个元素
            for right in range(1, l):
                if list[right] < list[idx]:
                    break
                elif list[right] > list[idx] and right+1 == l:
                        MainUnitList.append(list[idx])
                        MainUnit = MainUnit + 1
        if idx == l - 1:#最后一个元素
            for left in range(idx-1, -1, -1):
                if list[left] > list[idx]:
                    break
                elif list[left] < list[idx] and left == 0:
                    MainUnitList.append(list[idx])
                    MainUnit = MainUnit + 1
        if idx > 0 and idx < l - 1: #中间元素
            for left in range(idx - 1, -1, -1):
                if list[left] > list[idx]:
                    break
                elif left == 0:
                    leftok = True
            if leftok is True:
                for right in range(idx+1, l):
                    if list[right] < list[idx]:
                        break
                    elif right + 1 == l:
                        MainUnitList.append(list[idx])
                        MainUnit = MainUnit + 1

    print(str(MainUnit))
    s = str(MainUnitList).replace('[', '').replace(']', '').replace(',', ' ').replace('\n', '')
    print(s)

list = eval(input())
fastsort(list)


#Solution 2
l = list(map(int, input().split()))
length = len(l)
ll = []
if len(l) == 1:
    print(1)
    print(l[0])
else:
    for i in range(1, length - 1):
        if l[i] > max(l[:i]) and l[i] < min(l[i+1:]):
            ll.append(l[i])
    if l[0] < l[1]:
            ll.append(l[0])
    if l[-1] > l[-2]:
            ll.append(l[-1])
    ll.sort()
    print(len(ll))
    print("".join([str(i) for i in ll]))