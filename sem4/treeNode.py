class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (float/int/str)
        self.left = left    # Left child
        self.right = right  # Right child
        self.balanceFactor = None
    def __str__(self):
        return str(self.value)
            

    