
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
my_graph.add_edges("Aidan", "David")

# Display vertices
print(my_graph.vertices)

