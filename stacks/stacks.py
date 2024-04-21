# Stacks - using singly linked lists

class Node:
    def __init__(self, data):
        # Set the value of the node and the next node to null
        self.value = data
        self.next = None

class Stack:
    def __init__(self):
        # Set the head with a null value
        self.top = None

    # Implement the push method
    def push(self, data):
        # Create new node
        new_node = Node(data)

        # Check whether the stack has a top node
        if self.top:
            # Point the next node of the new node to the top
            new_node.next = self.top
        self.top = new_node

    # Implement the pop method
    def pop(self):
        # Check whether the stack has a top node
        if self.top is None:
            return None
        else:
            # Store the popped node
            popped_node = self.top
            # The "next" node of the top becomes the new top node
            self.top = self.top.next
            popped_node.next = None
            # Return the popped node
            return popped_node.data
    
    # Implement the peek method
    def peek(self):
        # Check whether the stack has a top node
        if self.top:
            return self.top.data
        else:
            return None


print("Stacks - using singly linked lists")
# Create a stack object
stack = Stack()

# Push elements to the stack
stack.push(3)
print(stack.top.value)  # Output: 1

# Pop elements from the stack
print(stack.pop())  # Output: 1

# Peek the top element of the stack
print(stack.peek())  # Output: None
