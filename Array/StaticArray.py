"""
Class that represents a simple static array structure with basic functionalities

A static array has a FIXED capacity that cannot change after initialization
When elements are removed, they are shifted left and None is placed at the end
to maintain the fixed size. This is different from dynamic arrays which can grow
"""
from Array import Array

class StaticArray(Array):
    """
    Static array implementation with fixed capacity
    
    Key characteristics:
    - Fixed size (capacity) set at initialization
    - Cannot grow beyond capacity
    - Removing elements shifts remaining elements left
    - Empty slots are filled with None
    """
    
    def __init__(self, capacity_or_list):
        """
        Initialize a static array
        
        Can be initialized in two ways:
        1. With an integer capacity: StaticArray(5) -> creates empty array of size 5
        2. With a list: StaticArray([1,2,3]) -> creates array with those elements
        
        Args:
            capacity_or_list: Either an integer capacity or a list of initial values
        """
        super().__init__()
        
        if isinstance(capacity_or_list, int): #If given an integer, create empty array with that capacity
            self._capacity = capacity_or_list
            self._items = [None] * capacity_or_list
            self._length = 0
        else:
            #If given a list, use it to initialize the array and make a copy to avoid modifying the original
            initial_list = capacity_or_list
            self._capacity = len(initial_list)
            self._items = initial_list.copy()
            self._length = len(initial_list)
    
    def is_full(self) -> bool:
        """
        Check if the static array is at full capacity
        
        Returns:
            bool: True if array is full, False otherwise
        """
        return self._length == self._capacity
    
    def insert(self, item) -> bool:
        """
        Insert an item into the static array.
        
        If index is provided, overrides the item at that index
        If index is None, appends to the end
        
        Args:
            item: The item to insert
            index: Optional index position (defaults to end if None)
            
        Returns:
            bool: True if insertion was successful, False if array is full
        """
        if self.is_full():
            return False
        
        self._items[self._length] = item
        self._length += 1
        return True
    
    def remove(self, index: int) -> bool:
        """
        Remove an item from the static array at the given index
        
        Args:
            index: The index of the item to remove
            
        Returns:
            bool: True if removal was successful, False if index is invalid
        """
        if not self.isCorrectIndex(index):
            return False
        
        for i in range(index, self._length - 1):
            self._items[i] = self._items[i + 1]
        
        self._items[self._length - 1] = None
        self._length -= 1
        return True
    
    def get(self, index: int):
        """
        Get the item at the given index.
        
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
        Set the value at the given index.
        
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
        Return a string representation of the static array.
        Shows elements and capacity
        
        Returns:
            str: String representation showing elements and capacity
        """
        return f"StaticArray{str(self._items)} (capacity: {self._capacity}, length: {self._length})"
    