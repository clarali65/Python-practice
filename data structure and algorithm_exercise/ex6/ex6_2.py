def topKFrequent(nums, k):
    idict = {}
    Klist = []
    Kdict = {}
    for i in nums:
        if i in idict:
            idict[i] = idict[i] + 1
        else:
            idict[i] = 0
            idict[i] = idict[i] + 1
    a = sorted(idict.items(), key=lambda x: x[1], reverse=True)
    if len(a) < k:
        print(" ".join(str(i[0]) for i in a))
    else:
        a = a[:k]
        print(" ".join(str(j[0]) for j in a))
lst = eval(input())
k = int(input())
topKFrequent(lst, k)