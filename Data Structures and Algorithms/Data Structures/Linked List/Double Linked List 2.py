# Linked List - Doubly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.nxt=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_if_ll_isempty(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            print("Linked List is not Empty")

    def add_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nxt=self.head
            self.head.prev=new_node
            self.head=new_node
    
    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nxt is not None:
                n=n.nxt
            n.nxt=new_node
            new_node.prev=n
            # self.tail=new_node
    
    def add_after(self,prev_node_data,data):
        new_node=Node(data)
        tail=self.tail_()
        if self.head is None:
            print("Linked List is Empty")
        elif tail.data==prev_node_data:
            self.add_at_end(data)
        else:
            n=self.head
            while n.nxt is not None:
                if n.data==prev_node_data:
                    break
                n=n.nxt
            else:
                print("There is no such previous data in the Linked List")     
            new_node.nxt =n.nxt
            new_node.prev=n
            n.nxt.prev=new_node
            n.nxt=new_node
        
    def remove_at_beginning(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            head_nxt=self.head.nxt
            self.head=head_nxt
            self.head.prev=None

    def remove(self,data_to_be_deleted):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n is not None:
                if n.data==data_to_be_deleted:
                    break
                prev=n
                n=n.nxt
            else:
                print("There is no such element in the Linked List")
            prev.nxt=n.nxt
            n.nxt.prev=prev

    def remove_after(self,prev_node_data):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n.nxt is not None:
                nxt=n.nxt
                if n.data==prev_node_data:
                    break
                n=n.nxt
            else:
                print("There is no such previous node data in Linked List")
            n.nxt=nxt.nxt
            nxt.prev=n

    def remove_at_end(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            n=self.head
            while n.nxt is not None:
                n=n.nxt
            n.prev.nxt=n.nxt
            self.tail=n.prev
            
    def traversal(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            print()
            print("Forward Traversal :")
            n=self.head
            while n is not None:
                if n.prev is None and n==self.head:
                    print("None <===",n.data,"===>",end=" ")
                elif n.nxt is None:
                    print("<==",n.data,"===> None",end=" ")
                else:
                    print("<===",n.data,"===>",end=" ")
                n=n.nxt
            print()

    def traversal_backward(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            print()
            print("Backward Traversal :")
            n=self.head
            while n.nxt is not None:
                n=n.nxt
            while n is not None:
                if n.nxt is None:
                    print("None <===",n.data,"===>",end=" ")
                elif n == self.head:
                    print("<===",n.data,"===> None",end=" ")
                else:
                    print("<===",n.data,"===>",end=" ")
                n=n.prev
            print()

    def head_of_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            print(f"The Head of Doubly Linked List is {self.head.data}")

    def tail_of_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            tail=self.tail_()
            print(f"The Tail of Doubly Linked List is {tail.data}")
            
    def tail_(self):
        n=self.head
        if self.head.
        while n.nxt is not None:
            prev=n
            n=n.nxt
        self.tail=n
        self.tail.prev=prev
        return self.tail

dll=DoublyLinkedList()
dll.add_at_beginning(20)
dll.add_at_beginning(3)
dll.add_at_beginning(2)
dll.add_at_beginning(1)
dll.add_at_beginning(0)
dll.add_at_beginning(-1)
dll.add_after(3,4)
dll.add_after(20,10)
dll.add_at_end(40)
dll.add_at_end(60)
dll.add_if_ll_isempty(899)
dll.remove_at_beginning()
dll.remove_at_beginning()
dll.remove_at_beginning()
dll.remove_at_beginning()
dll.remove_at_beginning()
dll.remove(40)
dll.remove_at_end()
dll.traversal()
dll.traversal_backward()
dll.head_of_ll()
dll.tail_of_ll()
# print(dir(dll)) #'add_after', 'add_at_beginning', 'add_at_end', 'add_if_ll_isempty','remove_at_beginning',
                 # 'remove','remove after','head_of_ll',tail_of_ll', 'traversal', 'traversal_backward'
