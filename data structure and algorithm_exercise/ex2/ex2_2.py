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

def func(mylist):
    q = Queue()
    output = []
    new_list = []
    temp = 0
    for i in mylist:
        q.enqueue(i)
    while temp < len(mylist):
        first = q.dequeue()
        new_list.append(first)
        while new_list[-1] - new_list[0] > 10000:
            new_list.pop(0)
        output.append(len(new_list))
        temp = temp + 1
    return output

mylist = eval(input())
print(func(mylist))