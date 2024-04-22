# Working with Stacks

## Stacks
- Follows **LIFO**: Last in First Out
    - Last inserted item will be the first item to be removed
- Can only **add** at the top
    - **Pushing** onto the stack
```python
# Initialize Node
class Node:
    def __init__(self, data):
        # Set the value of the node and the next node to null
        self.value = data
        self.next = None
```

```python
# Initialize Stack
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

```

- Can only **remove** from the top
    - **Popping** from the stack

```python
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

```
- Can only **read** the last element
    - **peeking** from the stack
```python
# Implement the peek method
    def peek(self):
        # Check whether the stack has a top node
        if self.top:
            return self.top.data
        else:
            return None
```

## Stacks real uses
- Undo functionality
- Symbol Checker: ([{}])
- Function Calls


