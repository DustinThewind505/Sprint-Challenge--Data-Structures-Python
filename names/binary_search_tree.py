class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:

            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True

        elif target < self.value:
            if self.left:
                return self.left.contains(target)

        else:
            if self.right:
                return self.right.contains(target)

        return False

    def get_max(self):
        current_node = self

        while current_node.right:
            current_node = current_node.right

        return current_node.value

    def for_each(self, fn):

        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)