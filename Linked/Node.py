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
    def __init__(self, value:any):
        self.value = value
        self.next = None

    def __str__(self):
        """
        Return a string representation of the node
        """
        return str(self.value)

    def __repr__(self):
        """
        Return a string representation of the node
        """
        return f"Node({self.value})"

class DoubleLinkedNode(Node):
    """
    Doubly node implementation
    
    Key characteristics:
    - Each node contains a value and a pointer to the next and previous node
    """
    def __init__(self, value):
        super().__init__(value)
        self.previous = None

    def __str__(self):
        """
        Return a string representation of the node
        """
        return str(self.value)

    def __repr__(self):
        """
        Return a string representation of the node
        """
        return f"DoubleLinkedNode({self.value})"