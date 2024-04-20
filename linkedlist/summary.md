# Linked List Implementation in Python

## Node Class
- Defines a node in the linked list.
- Each node has a `value` representing the data it holds and a `next` pointer pointing to the next node in the list.
- Initialized with the `data` value and `next` pointer set to `None`.

```python
class Node:
    def __init__(self, data):
        # Set the value of the node and the next node to null
        self.value = data
        self.next = None
```

## LinkedList Class

    - Initializes the linked list with head and tail set to None.
    - Provides a method insert_at_beginning to insert a new node at the beginning of the list.
        - If the list is empty, both head and tail point to the new node.
        Otherwise, the new node becomes the new head, and its next points to the previous head.
    - Provides a method remove_at_beginning to remove the node at the beginning of the list.
        - Updates the head to point to the next node, effectively removing the current head node.

```python
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
```

## Usage

    - Create a linked list object using LinkedList().
    - Check the initial state of the linked list (head and tail are None).
    - Insert a node at the beginning using insert_at_beginning.
    - Check the updated state of the linked list.
    - Remove a node from the beginning using remove_at_beginning.
    - Check the updated state of the linked list.

```python
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
```