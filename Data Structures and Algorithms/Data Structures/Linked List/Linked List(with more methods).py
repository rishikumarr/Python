class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_last(self, data):
        if self.head == None:
            self.head=Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data,None)

    def insert_values(self, list):
        self.head = None
        for item in list[::-1]:
            node = Node(item, self.head)
            self.head = node

    def print(self):
        if self.head == None:
            print("Linked List Is Empty")
        itr = self.head
        llstr=""
        while itr:
            llstr += str(itr.data) + "---->"
            itr = itr.next
        print(llstr)

    def insert_after_value(self, x, value_after_x):
        if self.head == None:
            print("Linked List is Empty")
        itr = self.head
        try:
            while itr.data!=x:
                itr = itr.next
            node=Node(value_after_x, itr.next)
            itr.next = node
        except:
            print("x value not in Linked List")

    def length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr=itr.next
        return length

    def remove_by_value(self, x):
        if self.head == None:
            print("Linked List is Empty")
        count=0
        itr = self.head
        while itr.data != x:
            count += 1
            previous=itr
            itr = itr.next
        itr=previous
        itr.next = itr.next.next
    
    def remove_at(self,index):
        if self.head is None:
            print("Linked List Is Empty")
        count = 0
        itr = self.head
        while itr:
            if count == index :
                item_at_index = itr.data
                self.remove_by_value(item_at_index)
                break
            count += 1
            itr = itr.next
            
    def insert_value_at(self, index, item):
        if self.head is None:
            print("Linked List Empty")
        if index < 0 or index > self.length():
            print("Invalid Index")
        if index == 0:
            self.insert_at_beginning(item)
        if index == self.length()-1:
            self.insert_at_last(item)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(item, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_values_at(self, index, list):
        if index < 0 or index > self.length():
            print("Invalid Index")
        if index == 0:
            for item in list[::-1]:
                node = Node(item, self.head)
                self.head=node
        if self.head == None:
            print("Linked List is Empty")
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                for i in list[::-1]:
                    node = Node(i, itr.next)
                    itr.next = node
                break
            itr = itr.next
            count+=1

ll = LinkedList()
ll.insert_values([1, 2, 4, 5]) # clear all if any values in linked list and insert values
ll.insert_value_at(2, 3)  # insert value at specified index
print(ll.length())  # returns the length of linked list
ll.insert_value_at(5, 7) 
ll.remove_at(5)  # remove item at given index
ll.insert_at_beginning(0) # insert item at beginning of linked list
ll.insert_values_at(0, [-7,-6,-5, -4, -3, -2, -1])  # insert values at given index
ll.insert_after_value(5, 6)  # insert passed value after passed item(x)
ll.insert_at_last(7)  # insert passed item at last 
ll.insert_at_last(9)
ll.remove_by_value(9)  # remove the passed item from linked list
ll.print() # print the entire linked list
