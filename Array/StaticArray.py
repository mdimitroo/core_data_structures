"""
Class that represents a simple static array structure with basic functionalities.
"""

class StaticArray:
    def __init__(self, size:int):
        self.items = []
        self.length:int = 0
        self.size:int = size

    def __init__(self, list):
        self.items = list
        self.length:int = len(list)
        self.size:int = len(list)

    def is_empty(self) -> bool:
        return self.length == 0
    
    def is_full(self) -> bool:
        return self.length == self.size
    
    def insert(self, item) -> bool:
        if self.is_full():
            return False
        self.items.append(item)
        self.length += 1
        return True
    
    def remove(self, index) -> bool:
        if not self.__isCorrectIndex(index):
            return False
        self.items.pop(index)
        self.length -= 1
        return True
    
    def get(self, index):
        if not self.__isCorrectIndex(index):
            return None
        return self.items[index]
    
    def __isCorrectIndex(self, index) -> bool:
        return 0 <= index < self.length
    
    def __str__(self) -> str:
        return str(self.items)
    
    def __len__(self) -> int:
        return self.length
    
    def clear(self):
        self.items = []
        self.length = 0

    
