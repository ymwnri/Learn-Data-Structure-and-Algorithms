class Node:
    def __init__(self, data):
        # Set the value of the node and the next node to null
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Set the head and the tail with null values
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Create the new node
        new_node = Node(data)
        # Check whether the linked list has a head node
        if self.head:
        # Point the next node of the new node to the head
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node      
            self.head = new_node
    
    def remove_at_beginning(self):
        # The "next" node of the head becomes the new head node
        self.head = self.head.next

# Create a linked list object
linked_list = LinkedList()

# Check the initial state of the linked list
print(linked_list.tail)
print(linked_list.tail)

# Insert a node at the beginning
linked_list.insert_at_beginning(1)

# Check the updated state of the linked list
print(linked_list.head.value)  # Output: 1
print(linked_list.tail.value)  # Output: 1

# Remove a node from the beginning
linked_list.remove_at_beginning()

# Check the updated state of the linked list
print(linked_list.head)  # Output: None

