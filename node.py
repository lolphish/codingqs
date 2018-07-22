class node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        if not self.left and not self.right:
            return str(self.val)
        children = []
        children.append(repr(self.left) if self.left else None)
        children.append(repr(self.right) if self.right else None)
        return str(self.val) + str(children)
