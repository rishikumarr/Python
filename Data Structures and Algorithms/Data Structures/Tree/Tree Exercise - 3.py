class Location:
    def __init__(self, place):
        self.place = place
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.place)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_tree():
    # Root
    root = Location("Global")

    # parent of gujarat and karnataka, children of global
    india = Location("India")

    # Gujarat(parent)(children of india)
    gujarat = Location("Gujarat")
    gujarat.add_child(Location("Ahmadebad"))
    gujarat.add_child(Location("Baroda"))
    
    # Karnataka(parent)(children of india)
    karnataka = Location("Karnataka")
    karnataka.add_child(Location("Bangalore"))
    karnataka.add_child(Location("Mysore"))
    
    # India
    india.add_child(gujarat)
    india.add_child(karnataka)

    # USA
    usa = Location("USA")

    # New Jersey(parent)
    new_jersey=Location("New Jersey")
    new_jersey.add_child(Location("Princeton"))
    new_jersey.add_child(Location("Trenton"))
    
    # California(parent)
    california=Location("California")
    california.add_child(Location("San Francisco"))
    california.add_child(Location("Mountain View"))
    california.add_child(Location("Palo Alto"))

    #USA's children
    usa.add_child(new_jersey)
    usa.add_child(california)

    # Global (root)
    root.add_child(india)
    root.add_child(usa)
    return root

tree = build_tree()
# tree.print_tree(1)
# tree.print_tree(2)
tree.print_tree(3)


    
