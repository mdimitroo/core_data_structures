"""
Class that represents a dynamic array structure with automatic resizing

A dynamic array is a wrapper around Python's built-in list
It uses Python's list methods (append, insert, pop) which handle
all the resizing automatically
"""
from Array import Array

class DynamicArray(Array):
    """
    Dynamic array implementation - wrapper around Python's built-in list
    
    Key characteristics:
    - Can grow and shrink dynamically
    - Uses Python's list internally, which handles all resizing automatically
    - Simple wrapper that delegates to list methods
    """
    
    def __init__(self, initial_list=None):
        """
        Initialize a dynamic array
        
        Args:
            initial_list: Optional list of initial values (defaults to empty)
        """
        super().__init__()
        if initial_list is None:
            self._items = []
        else:
            self._items = list(initial_list)  #Make a copy to avoid modifying original
        self._length = len(self._items)
    
    def insert(self, item) -> bool:
        """
        Insert an item into the dynamic array
        
        If index is provided, inserts at that position (shifts elements right)
        If index is None, appends to the end using Python's append() method
        
        Args:
            item: The item to insert
            index: Optional index position (defaults to end if None)
            
        Returns:
            bool: True if insertion was successful, False if index is invalid
        """
        self._items.append(item)
        self._length += 1
        return True
    
    def remove(self, index: int) -> bool:
        """
        Remove an item from the dynamic array at the given index
        
        Uses Python's pop() method which automatically shifts elements
        
        Args:
            index: The index of the item to remove
            
        Returns:
            bool: True if removal was successful, False if index is invalid
        """
        if not self.isCorrectIndex(index):
            return False
        self._items.pop(index)
        self._length -= 1
        return True
    
    def get(self, index: int):
        """
        Get the item at the given index
        
        Args:
            index: The index to retrieve from
            
        Returns:
            The item at the index, or None if index is invalid
        """
        if not self.isCorrectIndex(index):
            return None
        return self._items[index]
    
    def set(self, index: int, value) -> None:
        """
        Set the value at the given index
        
        Args:
            index: The index to set
            value: The value to set at that index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if not self.isCorrectIndex(index):
            raise IndexError(f"Index {index} is out of bounds for array of length {self._length}")
        self._items[index] = value
    
    def __str__(self) -> str:
        """
        Return a string representation of the dynamic array
        Shows the actual elements and current length
        
        Returns:
            str: String representation showing elements and length
        """
        return f"DynamicArray{str(self._items)} (length: {self._length})"
