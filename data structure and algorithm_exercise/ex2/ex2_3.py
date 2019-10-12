def func(mylist):
    new_list = []
    i = 0
    n = 1
    max_num = max(mylist)
    while max_num >= 10 ** n:
        n = n+1
    while i < n:
        bucket = {}
        for x in range(10):
            bucket.setdefault(x, [])
        for x in mylist:
            radix = int((x / (10 ** i)) % 10)
            bucket[radix].append(x)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    mylist[j] = y
                    j = j + 1
        i = i + 1
    return mylist

if __name__ == '__main__':
mylist = eval(input())
print(func(mylist))