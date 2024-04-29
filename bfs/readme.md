# BFS 

## BFS - Binary trees
- Starts from the root 
- Visits every node of every level
```python
# BFS - binary trees
import queue

# BFS - binary trees
import queue

# Node class to represent a node in the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BinaryTree class to represent the binary tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if self.root:
            # Initialize a queue to keep track of nodes to visit
            visited_nodes = []
            bfs_queue = queue.SimpleQueue()
            bfs_queue.put(self.root)

            # run until queue is empty
            while not bfs_queue.empty():

                # Get the next node to visit
                current_node = bfs_queue.get()
                visited_nodes.append(current_node.data)

                if current_node.left:
                    bfs_queue.put(current_node.left)

                if current_node.right:
                    bfs_queue.put(current_node.right)
            return visited_nodes


# Example usage:
if __name__ == "__main__":
    # Example binary tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Breadth-First Search (BFS):")
    print(tree.bfs())  # Output: [1, 2, 3, 4, 5]
```

## BFS - graph
- Graphs can have cycle
    - Needs to check if vertices have already been visited


## BFS vs DFS
BFS
- Target is close to starting vertex
- Applications
    - Web crawling
    - Finding shortest path in unweighted graphs
    - Connected locations using GPS
- Used as part of other more complex algorithm

DFS
- Target is far away from starting vertex
- Applications
    - Solving puzzles with one solution (e.g. mazes)
    - Detecting cycles in graphs
    - shortest path in a weighted graph
- Used as part of other more complex algorithm
