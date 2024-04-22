# Create class Treenode
class TreeNode:

    # Initialize Nodes
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


# Input data to tree node
node_1 = TreeNode("B")
node_2 = TreeNode("C")
root_node = TreeNode("A", node_1, node_2)

# Display A B C
print(root_node.data, node_1.data, node_2.data)