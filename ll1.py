class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node

    def traverse(self):
        """Traverse and print all the elements in the linked list."""
        current = self.head
        while current:  # Continue until the end of the list
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    print("Linked List Traversal:")
    ll.traverse()
