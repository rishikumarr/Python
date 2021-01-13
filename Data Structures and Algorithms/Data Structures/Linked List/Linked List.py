# Linked List - Singly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            head=self.head
            self.head=new_node
            new_node.nxt=head

    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nxt is not None:
                n=n.nxt
            n.nxt=new_node

    def add_after(self,previous_node_data,data):
        new_node=Node(data)
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n.nxt is not None:
                if n.data==previous_node_data:
                    break
                n=n.nxt
            else:
                print("There's no such element in Linked List")
            # print(n.data) # It prints the 'previous_node_data" passed to the function
            next=n.nxt # previous node's next
            n.nxt=new_node
            new_node.nxt=next

    def remove_at_beginning(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            curr_head_nxt=self.head.nxt # current self.head.nxt
            self.head=curr_head_nxt

    def remove_at_end(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            # tail=self.tail_ 
            # self.remove(tail)
            # Alternate 
            n=self.head
            while n.nxt is not None:
                prev=n
                n=n.nxt
            self.tail=prev.nxt
            prev.nxt = None

    def remove(self,data):
        if self.head is None:
            print("Linked List is Empty")
        elif self.head.data==data:
            self.remove_at_beginning()
        else:
            n=self.head
            while n.nxt is not None:
                if n.data==data:
                     break
                else:
                    prev_node=n
                n=n.nxt
            else:
                print("There's no such element in Linked List") 
            cur_node_nxt=n.nxt
            prev_node.nxt=cur_node_nxt
                    
    def traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n.nxt is not None:
                print(n.data,"--->",end=" ")
                n=n.nxt
            print(n.data,"---> None")
    
    def reverse_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            curr=self.head
            prev=None
            while curr!= None:
                next=curr.nxt
                curr.nxt=prev
                prev=curr
                curr=next
            self.head=prev
            n=self.head
            print("\nReversed Linked List:")
            while n.nxt is not None:
                print(n.data,"--->",end=" ")
                n=n.nxt
            print(n.data,"---> None ",end=" ")


    def print_rev(self,head):
        n=head
        while n is not None:
            print(n.nxt,"<---",end=" ")
            n=n.nxt

    def head_of_ll(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            print(f"The Head of Linked List is {self.head.data}")

    def tail_of_ll(self):
        tail=self.tail_()
        print(f"The Tail of Linked List is {tail}")

    def tail_(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n.nxt is not None:
                n=n.nxt
            self.tail=n.data
            return self.tail


ll=LinkedList()
ll.add_at_beginning(-1)
ll.add_at_beginning(-2)
ll.add_at_beginning(-3)
ll.add_at_end(1)
ll.add_at_end(2)
ll.add_at_end(3)
# ll.traversal()
ll.add_after(-1,0) # if the previous node data present more than once,it'll place the passed data after the first occurence of previous node data
ll.add_after(-3,4)
# ll.traversal()
ll.remove(4) # if the data present more than once it only remove the first occurence,Removing occurs from (left to right)
ll.remove_at_beginning()
ll.remove(-3)
ll.remove_at_end()
ll.remove_at_end()
ll.add_at_end(2)
ll.traversal()
ll.head_of_ll()
ll.tail_of_ll()
ll.add_at_end(3)
ll.reverse_ll()
# print(dir(ll)) #['add_after','add_at_beginning','add_at_end'
# 'head_of_ll','remove','remove_at_beginning','remove_at_end',
# 'tail_of_ll', 'traversal']