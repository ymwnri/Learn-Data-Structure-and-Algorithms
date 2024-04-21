# Implement a queue using a linked list
class Node:
    def __init__(self, data):
        # Set the value of the node and the next node to null
        self.value = data
        self.next = None

# Implement the Queue class
class Queue:
    def __init__(self):
        # Set the head and the tail with null values
        self.head = None
        self.tail = None

    # Implement the enqueue method
    def enqueue(self, data):
        # Create the new node
        new_node = Node(data)
        # Check whether the queue has a head node
        if self.head == None:

            # Point the next node of the new node to the head
            self.head = new_node
            self.tail = new_node
        else:
            # Point the next node of the tail to the new node
            self.tail.next = new_node
            self.tail = new_node

    # Implement the dequeue method
    def dequeue(self):
        
        # Check whether the queue has a head node
        if self.head:
            # Store the dequeued node
            current_node = self.head

            # The "next" node of the head becomes the new head node
            self.head = current_node.next

            # Next node of the current node is set to None
            current_node.next = None

            # Set the tail to None if the head is None
            if self.head is None:
                self.tail = None

