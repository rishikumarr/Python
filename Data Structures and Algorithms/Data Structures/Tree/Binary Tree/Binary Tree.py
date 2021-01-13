class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    def add_child(self, child):
        if child == self.data:
            return
        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BinaryTree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinaryTree(child)
    
    def inorder(self):
        inorder = []
        if self.left:
            inorder += self.left.inorder()
        inorder.append(self.data)
        if self.right:
            inorder += self.right.inorder()
        return inorder

    def preorder(self):
        preorder = [self.data]
        if self.left:
            preorder += self.left.preorder()
        if self.right:
            preorder += self.right.preorder()
        return preorder

    def postorder(self):
        postorder = []
        if self.left:
            postorder += self.left.postorder()
        if self.right:
            postorder += self.right.postorder()
        postorder.append(self.data)
        return postorder

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def sum_of_all(self):
        sum = 0
        sum+=self.data
        if self.left:
            sum += self.left.sum_of_all()
        if self.right:
            sum += self.right.sum_of_all()
        return sum
    
    def is_in(self, value):
        if value == self.data:
            return True
        if value < self.data:
            if self.left:
                return self.left.is_in(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.is_in(value)
            else:
                return False

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self

def build_tree(list):
    root = BinaryTree(list[0])
    for index in range(1, len(list)):
        root.add_child(list[index])
    return root

elements=[25,15,10,20,5]
binary_tree = build_tree(elements)
print(binary_tree.is_in(30))
binary_tree.delete(5)
print(binary_tree.inorder())
print("Inorder Traversal : {}".format(binary_tree.inorder())) #[5, 10, 15, 20, 25]
print("Pre order Traversal : {}".format(binary_tree.preorder())) #[25, 15, 10, 5, 20]
print("Post order Traversal : {}".format(binary_tree.postorder())) #[5, 10, 20, 15, 25]
print("Minimum Value in Binary Tree : {}".format(binary_tree.find_min())) # 5
print("Maximum Value in Binary Tree : {}".format(binary_tree.find_max())) # 25
print("Sum of all values in Binary Tree : {}".format(binary_tree.sum_of_all())) # 75
print()
alphabets = ["f", "c", "e", "b", "d", "a"]
binary_tree = build_tree(alphabets)
print(binary_tree.is_in("z"))
print("Inorder Traversal : {}".format(binary_tree.inorder())) #['a', 'b', 'c', 'd', 'e', 'f']
print("Pre order Traversal : {}".format(binary_tree.preorder())) #['f', 'c', 'b', 'a', 'e', 'd']
print("Post order Traversal : {}".format(binary_tree.postorder())) #['a', 'b', 'd', 'e', 'c', 'f']

