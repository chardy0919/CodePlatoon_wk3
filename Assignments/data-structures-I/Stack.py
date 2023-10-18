####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise
class Stack:
    def __init__(self):
        self.base = []

    def is_empty(self):
        return len(self.base) == 0

    def push(self, item):
        self.base.append(item)
           
    def pop(self):
        return self.base.pop()

    def peek(self):
        if self.base:
            return self.base[-1]
        return None
    
    def size(self):
        return len(self.base)

def rev_str(str):
    stack = Stack()
    for item in str:
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())
rev_str("string")



