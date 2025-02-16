class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1


        reverse.index(target)

    # def test_empty(self):
    #     '''Test Stack empty() method'''
    #     stk = Stack()
    #     assert(stk.isEmpty())
    #     assert(stk.size() == 0)
    #     assert(stk.pop() == None)
    #     stk.push(1)
    #     assert(not stk.isEmpty())
    #     assert(stk.size() == 1)
    #     assert(stk.pop() == 1)