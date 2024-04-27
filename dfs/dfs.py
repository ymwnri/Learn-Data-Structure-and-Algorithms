def dfs(graph, start, visited=None):
    """
    Perform Depth-First Search (DFS) on a graph.

    Parameters:
    - graph: The graph represented as an adjacency list.
    - start: The starting node for the DFS.
    - visited: A set to keep track of visited nodes. Default is None.

    Returns:
    - visited: The set of visited nodes.
    """

    if visited is None:
        visited = set()  # Initialize visited set if not provided

    visited.add(start)  # Mark current node as visited
    print(start, end=' ')  # Print the visited node

    # Explore all neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

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

    print("Depth-First Search (DFS):")
    dfs(graph, 'A')  # Starting DFS from node 'A'


# DFS using trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_tree(root):
    """
    Perform Depth-First Search (DFS) on a tree.

    Parameters:
    - root: The root node of the tree.

    Returns:
    - visited: The list of visited nodes.
    """

    visited = []  # List to keep track of visited nodes
    if root is None:
        return visited

    visited.append(root.value)  # Visit the current node

    # Recursively visit all children of the current node
    for child in root.children:
        visited.extend(dfs_tree(child))

    return visited

# Example usage:
if __name__ == "__main__":
    # Constructing a sample tree
    root = TreeNode('A')
    root.children = [TreeNode('B'), TreeNode('C'), TreeNode('D')]
    root.children[0].children = [TreeNode('E'), TreeNode('F')]
    root.children[2].children = [TreeNode('G')]

    print("Depth-First Search (DFS) on a tree:")
    print(dfs_tree(root))  # Starting DFS from the root node
