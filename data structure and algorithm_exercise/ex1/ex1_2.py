from pythonds.basic.stack import Stack
def dailyTemp(T):
    ans_list = []
    s = Stack()
    while abs(i) < len(T):
        if s.isEmpty() is True:
            s.push(i)
            ans_list[i] = 0
            i = i - 1
        else:
            if T[i] >= s.peek():
                s.pop()
                i = i - 1
            else:
                ans_list[i] = s.top() - i
                s.push(i)
                i = i - 1
    return ans_list

t = eval(input())
print(dailyTemp(t))