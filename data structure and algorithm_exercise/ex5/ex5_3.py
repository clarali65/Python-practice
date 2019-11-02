# insert and merge

def judge_insert(ori_list, sort_list):
    for step in range(1, len(ori_list)+1):
        a = one_step_insert(ori_list, step)
        if a == sort_list:
            print("Insertion Sort")
            print(one_step_insert(a))
    return False

def judge_merge(ori_list, sort_list):
    for step in range(1, len(ori_list)+1):
        b = one_step_merge(ori_list, step)
        if b == sort_list:
            print("Merge Sort")
            print(one_step_merge(a))

def one_step_insert(alist,step):
    index = step
    currentvalue = alist[index]
    position = index
    while alist[position - 1] > currentvalue and position > 0:
        alist[position] = alist[position - 1]
        alist[position - 1] = alist[position]
        position = position - 1
    alist[position] = currentvalue
    return insert

def one_step_merge(blist,step):
    step = 2 ** step #每次要比较的列表长度
    merge_step = len(blist)//step #一共要比较的次数
    for i in range(merge_step):
        for j in range(step - 1):
            if blist[j + i*step] > blist[j + i*step + 1]:
                blist[j + i*step],blist[j + i*step + 1] = blist[j + i*step + 1], blist[j + i*step]
    return blist

ori_list = eval(input())
sort_list = eval(input())
if judge_insert(ori_list, sort_list) == False:
    judge_merge(ori_list, sort_list)


# Solution 2
def check(lst1, lst2):
    flag = 0
    for i in range(len(lst2) - 1):
        if lst2[i] > lst2[i+1]:
            flag = i+1
            break
    if lst1[flag:] == lst2[flag:]:#插入排序
        result = sorted(lst1[:flag+1])+lst2[flag+1:]#再迭代一轮的结果
        return True, result
    else: #归并排序
        cnt = 2 #归并的数量
        result = lst2
        while result == lst2: #不断归并排序直到顺序发生变化
            sub_lst = [sorted(lst2[i:i+cnt]) for i in range(0, len(lst2), cnt)]
            result = [num for sub in sub_lst for num in sub]
            cnt = cnt * 2
        return False, result

lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
num = len(lst1)
flag, next_list = check((lst1, lst2))
if flag:
    print("Insertion Sort")
else:
    print("Merge Sort")
print(" ".join([str(i) for i in next_list]))