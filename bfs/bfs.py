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

# BFS - graphs
def bfs_graph(graph, initial_vertex):
    
    # Initialize a queue to keep track of nodes to visit
    visited_vertices = []
    bfs_graph = queue.SimpleQueue()
    bfs_graph.put(initial_vertex)

    # Add the initial vertex to the visited list
    visited_vertices.append(initial_vertex)

    # Run until the queue is empty
    while not bfs_graph.empty():
        
        # Get the next node to visit
        current_vertex = bfs_graph.get()

        # Visit all neighbors of the current node
        for neighbor in graph[current_vertex]:
            if neighbor not in visited_vertices:
                visited_vertices.append(neighbor)
                bfs_graph.put(neighbor)
    return visited_vertices


# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Breadth-First Search (BFS):")
    print(bfs_graph(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']