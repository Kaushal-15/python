class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class single():
    def __init__(self):
        self.head=None
    
    def __repr__(self):#repr is a represnting the list i.e traversal of the linked list
        pass
        
    def __contains__(self):#contains is used to check that the value contains in the linked list
        pass

    def __len__(self):
        pass

#O(n) linear time complexity because to append we want to go through all the list
    def append(self,value):
        if self.head is None:
            self.head= Node(value)
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=Node(value)
#0(1)-constant time complexity beacuse i am gonna add only in the head node which is frist and best case 
    def prepend(self,value):
        first_node=Node(value)
        first_node.next=self.head
        self.head=first_node

    def insert(self,value,index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounce")
            else:
                pass

    def delete(self,value):
        pass

    def pop(self,index):
        pass

    def get(self,index):
        pass

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__=="__main__":
    s=single()
    s.append(2)
    s.append(3)
    s.print()
    s.prepend(4)
    s.print()
    
