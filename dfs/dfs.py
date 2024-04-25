# In-order Traversal of a Binary Tree
# Time Complexity: O(n)
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=' ')
        in_order_traversal(root.right)

print("In-order Traversal of the Binary Tree: ", end='')
in_order_traversal(10)
