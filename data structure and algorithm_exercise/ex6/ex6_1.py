def findAnagrams(s, p):
    s = list(s)
    p = list(p)
    mark = []
    for i in range(len(s)-3):
        l = len(p)
        if set(s[i:i+l]) == set(p):
            mark.append(i)
    if len(mark) == 0:
        print("None")
    print(" ".join(str(j) for j in mark))

s = input()
p = input()
findAnagrams(s, p)