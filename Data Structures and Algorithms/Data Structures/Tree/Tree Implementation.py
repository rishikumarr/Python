import colorama
class Tree:
    def __init__(self, data):
        self.data = data
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

    def print_tree(self):
        if self.get_level() == 0 or  self.get_level()==1 :
            spaces = ' ' * self.get_level() * 3
            print(colorama.Fore.RED + spaces + self.data + " :")
        else:
            spaces = " " * self.get_level() * 3
            print(colorama.Fore.GREEN+spaces+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = Tree("Electronics")

    Laptops = Tree("Laptops")
    Laptops.add_child(Tree("Mac"))
    Laptops.add_child(Tree("Asus"))
    Laptops.add_child(Tree("Lenovo"))

    Mobile = Tree("Mobile")
    Mobile.add_child(Tree("Iphone"))
    Mobile.add_child(Tree("Samsung"))
    Mobile.add_child(Tree("Redmi"))
    
    Tv = Tree("Tv")
    Tv.add_child(Tree("Sony"))
    Tv.add_child(Tree("Toshiba"))
    Tv.add_child(Tree("Haier"))

    root.add_child(Laptops)
    root.add_child(Mobile)
    root.add_child(Tv)

    root.print_tree()


build_tree()


