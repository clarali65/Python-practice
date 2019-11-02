# first bad version
N = 50
isBadVersion = eval(input())

def firstBadVersion(n):
    first = 1
    last = n
    found = False
    while found == False:
        mid = first + (first + last) // 2
        a = isBadVersion(mid)
        if a == False:
            first = mid + 1
        else:
            b = isBadVersion(mid - 1)
            if b == False:
                found = True
                return mid
            else:
                last = mid - 1
print(firstBadVersion(N))

firstBadVersion(N)

# Solution 2 暴力从头查找
N = int(input())
isBadVersion = eval(input())

def firstBadVersion(n):
    for i in range(1,n+1):
        if (isBadVersion(i)):
            return i
print(firstBadVersion(N))

#Solution3 二分查找提高效率
N = int(input())
isBadVersion = eval(input())

def firstBadVersion(n):
    left = 1
    right = n
    while(left < right):
        mid = left + (right - left) // 2
        if (isBadVersion(mid)):
            right = mid
        else:
            left = mid + 1
    return left
print(firstBadVersion(N))