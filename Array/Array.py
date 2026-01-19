"""
Abstract array class - Parent class for all other array implementations

This class provides common methods and attributes that are shared between static and dynamic arrays
Subclasses should implement the abstract methods according to their specific behavior
"""
from abc import ABC, abstractmethod

class Array(ABC):
    """
    Abstract base class for array implementations.
    
    This class defines the common interface and shared functionality
    for both static and dynamic arrays. It uses ABC (Abstract Base Class)
    to ensure subclasses implement required methods.
    """
    
    def __init__(self) -> None:
        """
        Initialize the array with empty items and zero length.
        Subclasses should call super().__init__() and then set up
        their specific attributes (like capacity for static arrays).
        """
        self._items = []  # Internal storage for array elements
        self._length = 0   # Current number of elements in the array

    def is_empty(self) -> bool:
        """
        Check if the array is empty.
        
        Returns:
            bool: True if array has no elements, False otherwise
        """
        return self._length == 0
    
    def __len__(self) -> int:
        """
        Return the current number of elements in the array.
        This allows using len(array) syntax.
        
        Returns:
            int: Number of elements currently in the array
        """
        return self._length
    
    def isCorrectIndex(self, index: int) -> bool:
        """
        Check if an index is valid for accessing elements.
        Valid indices are 0 to length-1 for both static and dynamic arrays.
        
        Args:
            index: The index to check
            
        Returns:
            bool: True if index is valid, False otherwise
        """
        return 0 <= index < self._length
    
    @abstractmethod
    def insert(self, item, index: int = None):
        """
        Insert an item into the array.
        Must be implemented by subclasses.
        
        Args:
            item: The item to insert
            index: Optional index position (behavior depends on subclass)
            
        Returns:
            bool: True if insertion was successful, False otherwise
        """
        pass

    @abstractmethod
    def remove(self, index: int):
        """
        Remove an item from the array at the given index.
        Must be implemented by subclasses.
        
        Args:
            index: The index of the item to remove
            
        Returns:
            bool: True if removal was successful, False otherwise
        """
        pass

    @abstractmethod
    def get(self, index: int):
        """
        Get the item at the given index.
        Must be implemented by subclasses.
        
        Args:
            index: The index to retrieve from
            
        Returns:
            The item at the index, or None if index is invalid
        """
        pass
    
    @abstractmethod
    def set(self, index: int, value) -> None:
        """
        Set the value at the given index.
        Must be implemented by subclasses.
        
        Args:
            index: The index to set
            value: The value to set at that index
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the array
        
        Returns:
            str: String representation of the array
        """
        return str(self._items)
    
    def clear(self) -> None:
        """
        Clear all elements from the array
        Resets length to 0
        """
        self._items = []
        self._length = 0