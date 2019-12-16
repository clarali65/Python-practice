def createHashTable(n):
    k = n
    for i in range(2, k//2 + 1):
        if k % i == 0:
            k = k + 1
    table = [None] * k
    return table

def insertNumber(table, nums):
    j = 1
    plist = []
    for i in nums:
        position = i % len(table)
        if table[position] == None:
            table[position] = i
            plist.append(position)
        elif table[position] == i:
            plist.append(position)
        else:
            while table[position] != None and table[position] != i:
                position = position + j
                j = j + 2
                if position > len(nums):
                    plist.append('-')
                    break
    print(" ".join(str(k) for k in plist))

n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumber(table, nums)