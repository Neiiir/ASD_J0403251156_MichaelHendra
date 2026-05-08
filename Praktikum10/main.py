class Node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d

    def insert(self, d):
        if self.data:
            if d < self.data:
                if self.left is None:
                    self.left = Node(d)
                else:
                    self.left.insert(d)

            if d > self.data:
                if self.right is None:
                    self.right = Node(d)
                else:
                    self.right.insert(d)
        else:
            self.data = d

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

def inorder(root):
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []

def preorder(root):
    return [root.data] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []

# DATA NIM 56
root = Node(56)
data = [36, 76, 26, 46, 66, 86, 41]

for d in data:
    root.insert(d)

print("NAMA : MICHAEL HENDRA")
print("NIM  : J0403251156")
print("============================================")
print("Inorder:", inorder(root))
print("Preorder:", preorder(root))
print("Post-order:", postorder(root))