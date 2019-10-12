class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# function1

def func(S):
    q = Queue()
    str_min = S
    temp = 0
    for i in S:
        q.enqueue(i)
    while temp <= q.size():
        a = q.dequeue()
        q.enqueue(a)
        new_list = ''.join(q.items)[::-1]
        if new_list < str_min:
            str_min = new_list
        temp = temp + 1
    return str_min


# function2

def func(S):
    min_str = S
    for i in range(len(S)):
        new_str = S[1:] + S[0]
        if new_str < min_str:
            min_str = new_str
    return min_str

S = eval(input())
print(func(S))