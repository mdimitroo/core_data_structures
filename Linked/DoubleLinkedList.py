"""
Class that represents a double linked list structure with basic functionalities

A double linked list is a collection of nodes that are linked together using pointers
Each node contains a value and a pointer to the next and previous node
The first and last nodes point to None
"""

from Linked.Node import DoubleLinkedNode

class DoubleLinkedList:
    """
    Double linked list implementation
    """
    def __init__(self):
        """
        Initialize an empty linked list
        """
        self._head = None
        self._length = 0

    def __len__(self):
        """
        Return the length of the linked list
        """
        return self._length

    def __str__(self):
        """
        Return a string representation of the linked list
        """
        return f"LinkedList({self._head})"

    def insert_at_beginning(self, value):
        """
        Insert a value at the beginning of the linked list
        """
        new_node = DoubleLinkedNode(value)
        new_node.next = self._head
        if self._head is not None:
            self._head.previous = new_node
        self._head = new_node
        self._length += 1
        return

    def insert_at_end(self, value:any):
        """
        Insert a value at the end of the linked list
        """
        new_node = DoubleLinkedNode(value)
        if self._head is None:
            self._head = new_node
            self._length += 1
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.previous = current
            self._length += 1
        return

    def insert_at_index(self, value:any, index:int):
        """
        Insert a value at the given index
        """
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_at_beginning(value)
        elif index == self._length:
            self.insert_at_end(value)
        else:
            # Move to the node BEFORE the insertion point
            new_node = DoubleLinkedNode(value)
            current = self._head
            for i in range(index - 1):
                current = current.next
            tmp = current.next
            new_node.next = tmp
            new_node.previous = current
            current.next = new_node
            tmp.previous = new_node
            self._length += 1
        return

    def delete_head(self):
        """
        Delete the head node from the linked list
        """
        if self._head is None:
            raise ValueError("Linked list is empty")
        if self._length == 1:
            self._head = None
            self._length = 0
        else:
            self._head = self._head.next
            self._head.previous = None
            self._length -= 1
        return
        
    def delete_tail(self):
        """
        Delete the tail node from the linked list
        """
        if self._head is None:
            raise ValueError("Linked list is empty")
        if self._length == 1:
            self._head = None
            self._length = 0
        else:
            current = self._head
            while current.next.next is not None:
                current = current.next
            current.next.previous = None
            current.next = None
            self._length -= 1
        return
    
    def delete_at_index(self, index:int):
        """
        Delete the node at the given index
        """
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.delete_head()
        elif index == self._length - 1:
            self.delete_tail()
        else:
            # Move to the node BEFORE the deletion point
            current = self._head
            for i in range(index - 1):
                current = current.next
            node_to_delete = current.next
            current.next = node_to_delete.next
            node_to_delete.next.previous = current
            self._length -= 1
        return

    def get_at_index(self, index:int):
        """
        Get the value at the given index
        """
        if index < 0 or index >= self._length:
            raise IndexError("Index out of bounds")
        current = self._head
        for i in range(index):
            current = current.next
        return current.value

    def search(self, value:any):
        """
        Search for the given value in the linked list
        """
        current = self._head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False