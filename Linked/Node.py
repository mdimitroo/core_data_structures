"""
Class that represents a node in a linked list
Each node contains a value and a pointer to the next node
The last node points to None
"""

class Node:
    """
    Node implementation
    
    Key characteristics:
    - Each node contains a value and a pointer to the next node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class DoubleLinkedNode(Node):
    """
    Doubly node implementation
    
    Key characteristics:
    - Each node contains a value and a pointer to the next and previous node
    """
    def __init__(self, value):
        super().__init__(value)
        self.previous = None