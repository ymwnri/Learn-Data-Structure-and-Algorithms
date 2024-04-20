# Summarization

## Node Class

    - Defines a node in the linked list.
    - Each node has a value representing the data it holds and a next pointer - pointing to the next node in the list.
    - Initialized with the data value and next pointer set to None.

## LinkedList Class

    - Initializes the linked list with head and tail set to None.
    - Provides a method insert_at_beginning to insert a new node at the beginning of the list.
        - If the list is empty, both head and tail point to the new node.
        Otherwise, the new node becomes the new head, and its next points to the previous head.
    - Provides a method remove_at_beginning to remove the node at the beginning of the list.
        - Updates the head to point to the next node, effectively removing the current head node.

## Usage

    - Create a linked list object using LinkedList().
    - Check the initial state of the linked list (head and tail are None).
    - Insert a node at the beginning using insert_at_beginning.
    - Check the updated state of the linked list.
    - Remove a node from the beginning using remove_at_beginning.
    - Check the updated state of the linked list.