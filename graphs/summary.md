## Graphs

# Graphs
- Set of nodes/verticles that is connected to another node/verticles through links/edges
- Trees are type of graph
- Directed graphs
    - Specified direction
- Undirected
    - No direction
    - relationship are mutual
- Weighted
    - numeric values with edges
    - can be either directed or undirected

# Trees vs Graph

Trees
- Cannot have cycles
- All nodes must be connected

Graph
- Can have cycles
- There can be unconnected nodes
- User relationship in social networks
    - friendship
    - follows
- Location and distances
    - optimize routes
- Graph and sorting algo

```python

# Create Graph Class
class Graph:

    # Initialize node
    def __init__(self):
        self.vertices = {}

    # Add vertex
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    # Add edge
    def add_edges(self, source, target):
        self.vertices[source].append(target)

# Create Graph Object
my_graph = Graph()

# Add vertices
my_graph.add_vertex("Aidan")
my_graph.add_vertex("Joshua")
my_graph.add_vertex("David")

# Add edges
my_graph.add_edges("Aidan", "Joshua")
my_graph.add_edges("Joshua", "David")
my_graph.add_edges("David", "Aidan")

# Display vertices
print(my_graph.vertices)


```