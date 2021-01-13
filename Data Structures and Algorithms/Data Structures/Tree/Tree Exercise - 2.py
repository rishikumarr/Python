class Company:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent=self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p=self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, wants="both"):
        if wants == "designation":
            value = "({})".format(self.designation)
        elif wants == "name":
            value = self.name
        else:
            value = "{} ({})".format(self.name, self.designation)

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+value)

        if self.children:
            for child in self.children:
                child.print_tree(wants) 

def build_tree():
    # Infrastructure head
    infra = Company("Vishwa", "Infrastructure Head")
    infra.add_child(Company("Dhaval","Cloud Manager"))
    infra.add_child(Company("Abhijit", "App Manager"))
    
    # Application Head
    app = Company("Aamir", "Application Head")
    
    # CTO
    cto = Company("Chinmay", "CTO")
    cto.add_child(infra)
    cto.add_child(app)

    # HR Head
    hr = Company("Gels", "HR Head")
    hr.add_child(Company("Peter", "Recruitment Manager"))
    hr.add_child(Company("Waqas", "Policy Manager"))
    
    # CEO (Root Node)
    CEO = Company("Nilupul", "CEO")
    CEO.add_child(cto)
    CEO.add_child(hr)

    return CEO

tree=build_tree()
tree.print_tree()
# tree.print_tree("designation")
# tree.print_tree("name")
    

