from pythonds.basic.stack import Stack
def isValid(s):
    s_stack = Stack()
    opens = "([{"
    closers = ")]}"
    for i in s:
        if i in "([{ ":
            s_stack.push(s_list[i]);
        elif i in ")]} ":
            if s_stack.isEmpty() is not True:
                if opens.index(s_stack.pop()) == closers.index(s_list[i]) is not True:
                    return False
            else:
                return False
        else:
            return False
    return True

print(isValid(input()))