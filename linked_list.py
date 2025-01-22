class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + ' --> '
            itr = itr.next
        print(lstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(6)
    ll.insert(7)
    ll.print()
