# Binary Search Trees

## BST
- Left subtree of node: values less that the node itself
- Right subtree of node: values greater than node itself
- Both subtrees must be binary search trees

# Functions
- Initialize Classes
```python
class TreeNode:
    def __init__(self, data, left=None, right=None):
        # Initialize Tree Node
        self.data = data
        self.left_child = left
        self.right_child = right
```
```python
class BinarySearchTree:
    def __init__(self):
        # Initialize Binary Search Tree
        self.root = None
```
- Insert
```python
def insert(self, data):
        # Insert Node

        # Create a new node with the given data
        new_node = TreeNode(data)

        # If the tree is empty, set the new node as the root
        if self.root == None:
            self.root = new_node
            return
        
        # If the tree is not empty, find the appropriate position to insert the new node
        current_node = self.root
        while True:
            if data < current_node.data:
                # If the data is less than the current node's data, move to the left child
                if current_node.left_child == None:
                    # If the left child is empty, insert the new node here
                    current_node.left_child = new_node
                    return
                else:
                    # If the left child is not empty, move to the left child and continue searching
                    current_node = current_node.left_child
            elif data > current_node.data:
                # If the data is greater than the current node's data, move to the right child
                if current_node.right_child == None:
                    # If the right child is empty, insert the new node here
                    current_node.right_child = new_node
                    return
                else:
                    # If the right child is not empty, move to the right child and continue searching
                    current_node = current_node.right_child 
```
- Search
```python
def search(self, search_value):
        # Search Node

        # Start searching from the root
        current_node = self.root

        # Loop until we reach a leaf node (or until we find the value)
        while current_node:
            if search_value == current_node.data:
                # If the search value is equal to the current node's data, return True
                return True
            elif search_value < current_node.data:
                # If the search value is less than the current node's data, move to the left child
                current_node = current_node.left_child
            elif search_value > current_node.data:
                # If the search value is greater than the current node's data, move to the right child
                current_node = current_node.right_child
        
        # If we reach here, the value was not found, so return False
        return False
```
