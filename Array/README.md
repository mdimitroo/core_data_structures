# Arrays

## Overview

An **array** is a fundamental data structure that stores elements in contiguous memory locations. Each element can be accessed directly using its index, making arrays one of the most efficient data structures for random access operations.

Arrays are the building blocks for many other data structures and are widely used in computer science due to their simplicity and performance characteristics.

## Key Characteristics

- **Contiguous Memory**: Elements are stored in adjacent memory locations
- **Index-based Access**: Elements can be accessed directly using their index (0-based indexing)
- **Homogeneous/ heterogeneous**: Can store elements of the same type or different types (depending on language)
- **Fixed or Dynamic Size**: Can have a fixed capacity (static) or grow/shrink dynamically

## Array Operations and Time Complexities

### Common Operations

| Operation | Description | Static Array | Dynamic Array |
|-----------|-------------|--------------|---------------|
| **Access (`get`)** | Get element at index `i` | O(1) | O(1) |
| **Update (`set`)** | Set element at index `i` | O(1) | O(1) |
| **Insert (`insert`)** | Add element to array | O(1)  | O(1) |
| **Remove (`remove`)** | Remove element at index `i` | O(1) best, O(n) worst | O(1) best, O(n) worst |
| **Search** | Find element in array | O(n) | O(n) |
| **Length (`__len__`)** | Get number of elements | O(1) | O(1) |
| **Empty Check (`is_empty`)** | Check if array is empty | O(1) | O(1) |
| **Clear (`clear`)** | Remove all elements | O(1) | O(1) |

\* *For static arrays, insertion is O(1) only if there's available space. If the array is full, insertion fails.*

### Detailed Complexity Analysis

#### Access (`get`) - O(1)
- **Best Case**: O(1) - Direct memory access using index
- **Average Case**: O(1) - Constant time regardless of array size
- **Worst Case**: O(1) - Always constant time

Arrays provide direct access to elements because:
- Memory addresses are calculated as: `base_address + (index × element_size)`
- No traversal needed, just a simple arithmetic operation

#### Update (`set`) - O(1)
- Similar to access, updating an element at a known index is O(1)
- No shifting or searching required

#### Insert (`insert`) - O(1) amortized / O(n) worst case

**Static Array:**
- **Best Case**: O(1) - Inserting at the end when space is available
- **Worst Case**: O(1) - If array is full, insertion fails (returns False)
- **Note**: Static arrays only support appending at the end

**Dynamic Array:**
- **Best Case**: O(1) - Appending when capacity is available
- **Worst Case**: O(n) - When resizing is needed (copying all elements to new array)
- **Amortized**: O(1) - Over many operations, the cost averages to O(1) due to exponential growth strategy

**Why O(n) worst case?**
When a dynamic array runs out of capacity, it must:
1. Allocate a new, larger array (typically 2x the current size)
2. Copy all existing elements to the new array
3. Add the new element

This copying operation takes O(n) time, but happens infrequently, leading to O(1) amortized complexity.

#### Remove (`remove`) - O(1) best case, O(n) worst case

**Both Static and Dynamic Arrays:**
- **Best Case**: O(1) - Removing the last element requires no shifting
  - **Static Array**: The loop `range(index, length-1)` is empty when `index == length-1`, so no shifting occurs
  - **Dynamic Array**: Python's `pop()` is O(1) when removing the last element
- **Average Case**: O(n) - Removing from middle requires shifting half the elements
- **Worst Case**: O(n) - Removing the first element requires shifting all `n-1` elements

**Why O(1) for last element?**
When removing the **last element** (index `length - 1`):
- **Static Array**: The range `range(length-1, length-1)` is empty, so the loop doesn't execute. It just sets the element to `None` and decrements length.
- **Dynamic Array**: Python's `list.pop()` is optimized for removing the last element and runs in O(1) time.

**Why O(n) for other positions?**
When removing an element at index `i` where `i < length - 1`:
1. All elements after index `i` must be shifted left by one position
2. This requires moving `n - i - 1` elements
3. In the worst case (removing first element), all `n-1` elements must be shifted

**Static Array Note**: After removal, the last position is set to `None` to maintain fixed capacity.

#### Search - O(n)
- Linear search through the array
- Must check each element until found or end is reached
- No better than O(n) for unsorted arrays

## Implementation Types

This directory contains two implementations of arrays:

### 1. Static Array (`StaticArray`)

A **static array** has a **fixed capacity** that is determined at initialization and cannot change afterward.

#### Characteristics

- **Fixed Size**: Capacity is set at creation and never changes
- **Memory Efficient**: No overhead for resizing operations
- **Predictable**: Memory usage is known and constant
- **Limited Flexibility**: Cannot grow beyond initial capacity

#### How It Works

```python
# Initialize with capacity
arr = StaticArray(5)  # Creates empty array with capacity 5

# Or initialize with a list
arr = StaticArray([1, 2, 3])  # Capacity = 3, length = 3
```

#### Insertion Behavior

- Only supports **appending** at the end
- If array is full, insertion **fails** (returns `False`)
- Time Complexity: O(1) when space is available

```python
arr = StaticArray([1, 2, 3])  # Capacity: 3, Length: 3
arr.insert(4)  # Returns False - array is full
```

#### Deletion Behavior

- Removing an element **shifts all subsequent elements left**
- The **last position is set to `None`** to maintain fixed capacity
- Time Complexity: O(n) due to shifting

**Example:**
```python
arr = StaticArray([1, 2, 3])  # [1, 2, 3]
arr.remove(1)                 # Remove element at index 1
# Result: [1, 3, None]  (capacity: 3, length: 2)
```

---

### 2. Dynamic Array (`DynamicArray`)

A **dynamic array** can **grow and shrink** automatically as elements are added or removed.

#### Characteristics

- **Flexible Size**: Can grow and shrink as needed
- **Automatic Resizing**: Handles capacity management internally
- **Memory Overhead**: May allocate more memory than currently used
- **High Flexibility**: Can grow indefinitely (within system limits)

#### How It Works

This implementation is a **wrapper around Python's built-in list**, which is itself a dynamic array. Python's list handles all the resizing logic automatically using an exponential growth strategy.

```python
# Initialize empty
arr = DynamicArray()

# Or initialize with a list
arr = DynamicArray([1, 2, 3])
```

#### Insertion Behavior

- Supports **appending** at the end
- Automatically **resizes** when capacity is exceeded
- Time Complexity: O(1) amortized, O(n) worst case (when resizing)

```python
arr = DynamicArray([1, 2, 3])
arr.insert(4)  # Automatically handles resizing if needed
# Result: [1, 2, 3, 4]
```

#### Deletion Behavior

- Removing an element **shifts all subsequent elements left**
- Array **automatically shrinks** if it becomes too empty (optional optimization)
- Time Complexity: O(n) due to shifting

**Example:**
```python
arr = DynamicArray([1, 2, 3])  # [1, 2, 3]
arr.remove(1)                   # Remove element at index 1
# Result: [1, 3]  (length: 2, capacity may be larger)
```

#### Resizing Strategy

Python's list (which DynamicArray wraps) uses:
- **Growth Factor**: Typically doubles capacity when full
- **Amortized O(1)**: Over many insertions, the cost averages to O(1)
- **Example**: Capacity grows as 4 → 8 → 16 → 32 → ...

---

## Comparison Table

| Feature | Static Array | Dynamic Array |
|---------|--------------|---------------|
| **Capacity** | Fixed at initialization | Grows/shrinks automatically |
| **Memory Usage** | Predictable, constant | Variable, may be larger than needed |
| **Insertion** | O(1) if space available, fails if full | O(1) amortized, always succeeds |
| **Deletion** | O(n), maintains capacity with None | O(n), may shrink capacity |
| **Use Case** | Known max size, memory-constrained | Unknown size, general purpose |
| **Complexity** | Simple, no resizing logic | More complex, handles resizing |