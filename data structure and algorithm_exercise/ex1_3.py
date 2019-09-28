from pythonds.basic.stack import Stack
def calc(tokens):
    s = Stack()
    for i in tokens:
        if i in "0123456789":
            s.push(i)
        else:
            if i in "+-*/":
                t2 = s.pop()
                t1 = s.pop()
                t3 = operation(t1, t2, i)
                s.push(t3)

def operation(token1,token2,operate):
    if operate == '+':
        return token1 + token2
    elif operate == '-':
        return token1 - token2
    elif operate == '*':
        return token1 * token2
    else:
        return int(token1 / token2)

print(calc(input().split()))