####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node

    # def search(self, value_to_find):
    #     current_node = self.head
    #     while current_node:
    #         if current_node.value == value_to_find:
    #             return current_node
    #         current_node = current_node.next
    #     return None

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.value == data:
                return current_node
            current_node = current_node.next
        return None

lister = LinkedList()
lister.insert(1)
lister.insert(2)
lister.insert(3)
lister.insert(4)
# lister.search(2)
print(lister.search(2))