####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise
class Fifo:
    def __init__(self):
        self.base = []

    def is_empty(self):
        return len(self.base) == 0

    def enqueue(self, item):#just like push
        self.base.append(item)
           
    def dequeue(self):
        return self.base.pop()

    def peek(self):
        if self.base:
            return self.base[-1]
        return None
    
    def size(self):
        return len(self.base)