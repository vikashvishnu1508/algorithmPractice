# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value <= self.value:
            if self.left is None:
                self.left = value
            else:
                return self.insert(self.left, value)
        else:
            if self.right is None:
                self.right = value
            else:
                return self.insert(self.righ, value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True
        elif value <= self.value:
            if self.left is None:
                return False
            else:
                if self.left == value:
                    return True
                else:
                    return self.contains(self.left, value)
        else:
            if self.right is None:
                return False
            else:
                if self.right == value:
                    return True
                else:
                    return self.contains(self.right, value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
