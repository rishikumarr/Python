class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print_tree(self):
        space=" "*self.get_level()*3
        prefix=space+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root=Tree("Data structures")

    pdt=Tree("Primitive Data Type")
    pdt.add_child(Tree("Integer"))
    pdt.add_child(Tree("Character"))
    pdt.add_child(Tree("Float"))
    pdt.add_child(Tree("String"))

    root.add_child(pdt)

    npdt=Tree("Non Primitive Data Type")

    ldt=Tree("Linear")
    ldt.add_child(Tree("Arrays"))
    ldt.add_child(Tree("Stacks"))
    ldt.add_child(Tree("Queues"))

    ll=Tree("Linked List")
    ll.add_child(Tree("Singly Linked List"))
    ll.add_child(Tree("Doubly Linked List"))
    
    cll=Tree("Circular Linked List")
    cll.add_child(Tree("Singly Circular Linked List"))
    cll.add_child(Tree("Doubly Circular Linked List"))
    
    ll.add_child(cll)
    ldt.add_child(ll)

    npdt.add_child(ldt)

    nldt=Tree("Non Linear")

    t=Tree("Trees")
    t.add_child(Tree("Binary Tree"))

    nldt.add_child(t)
    nldt.add_child(Tree("Graphs"))
    nldt.add_child(Tree("Hash Table"))

    npdt.add_child(nldt)

    root.add_child(npdt)

    root.print_tree()
    
build_tree()


