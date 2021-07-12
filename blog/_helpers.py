class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_data):
        self.next_node = new_data


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        
    def size(self):
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.get_next()
        return count
    
    def search(self, data):
        current = self.head
        found = False
        
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("You've reached the end of the list")
        return current.get_data(), True
    
    # when  a node is remove [1, 2, 3, 4] = [1, None, 3, 4]
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('That value cannot be found')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())