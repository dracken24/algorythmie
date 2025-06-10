'''
===============================================================================    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
              -------------------------------------------------                    */
               PROJET: <React Learning2>          PAR: Dracken24                   */
              -------------------------------------------------                    */
               CREATED: 10-6th-2025                                                */
               MODIFIED BY: Dracken24                                              */
               LAST MODIFIED: 10-6th-2025                                          */
              -------------------------------------------------                    */
               FILE: datastructure.py                                              */
              -------------------------------------------------                    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
===============================================================================    */
'''

import array
import collections
import sys

class datastructure:
    def __init__(self, type: type):
        self.static_array: StaticArray = StaticArray(type)
        self.dynamic_array: DynamicArray = DynamicArray()
        self.singly_linked_list: SinglyLinkedList = SinglyLinkedList()
        self.doubly_linked_list: DoublyLinkedList = DoublyLinkedList()

# ------------------------------------------------------------------- #

class StaticArray:
    def __init__(self, dtype: type):
        self.array: array.array = array.array(dtype)
        self.size: int = 0

    # get the value at the index
    def get(self, index: int) -> int:
        return self.array[index]

    # insert the value at the head
    def insert_head(self, value: int) -> None:
        self.array.insert(0, value)
        self.size += 1

    # insert the value at the middle
    def insert_mid(self, index: int, value: int) -> None:
        self.array.insert(index, value)
        self.size += 1

    # insert the value at the tail
    def insert_tail(self, value: int) -> None:
        self.array.append(value)
        self.size += 1

    # delete the value at the head
    def delete_head(self) -> None:
        self.array.pop(0)
        self.size -= 1

    # delete the value at the middle
    def delete_mid(self, index: int) -> None:
        self.array.pop(index)
        self.size -= 1

    # delete the value at the tail
    def delete_tail(self) -> None:
        self.array.pop()
        self.size -= 1

    # get the memory usage
    def memory_usage(self) -> int:
        return self.array.itemsize * self.size
    
    # get the size
    def size(self) -> int:
        return self.size

# ------------------------------------------------------------------- #

class DynamicArray:

    def __init__(self):
        self.list: list = list()

    # get the value at the index
    def get(self, index: int) -> any:
        return self.list[index]

    # insert the value at the head
    def insert_head(self, value: any) -> None:
        self.list.insert(0, value)

    # insert the value at the middle
    def insert_mid(self, index: int, value: any) -> None:
        self.list.insert(index, value)

    # insert the value at the tail
    def insert_tail(self, value: any) -> None:
        self.list.append(value)

    # delete the value at the head 
    def delete_head(self) -> None:
        self.list.pop(0)

    # delete the value at the middle
    def delete_mid(self, index: int) -> None:
        self.list.pop(index)

    # delete the value at the tail
    def delete_tail(self) -> None:
        self.list.pop()

    # get the memory usage
    def memory_usage(self) -> int:
        return sys.getsizeof(self.list)

# ------------------------------------------------------------------- #

class SinglyLinkedList:
    
    def __init__(self):
        self.deque: collections.deque = collections.deque()
        self.deque.maxlen = None

    # get the value at the index
    def get(self, index: int) -> any:
        return self.deque[index]

    # insert the value at the head
    def insert_head(self, value: any) -> None:
        self.deque.appendleft(value)

    # insert the value at the middle
    def insert_mid(self, index: int, value: any) -> None:
        self.deque.insert(index, value)

    # insert the value at the tail
    def insert_tail(self, value: any) -> None:
        self.deque.append(value)

    # delete the value at the head
    def delete_head(self) -> None:
        self.deque.popleft()

    # delete the value at the middle
    def delete_mid(self, index: int) -> None:
        self.deque.pop(index)

    # delete the value at the tail
    def delete_tail(self) -> None:
        self.deque.pop()

    # get the memory usage
    def memory_usage(self) -> int:
        return sys.getsizeof(self.deque)

# ------------------------------------------------------------------- #

class DoublyLinkedList:

    def __init__(self):
        self.deque: collections.deque = collections.deque()
        # self.deque.maxlen = None

    # get the value at the index
    def get(self, index: int) -> any:
        return self.deque[index]

    # insert the value at the head
    def insert_head(self, value: any) -> None:
        self.deque.appendleft(value)

    # insert the value at the middle
    def insert_mid(self, index: int, value: any) -> None:
        self.deque.insert(index, value)

    # insert the value at the tail
    def insert_tail(self, value: any) -> None:
        self.deque.append(value)

    # delete the value at the head
    def delete_head(self) -> None:
        self.deque.popleft()

    # delete the value at the middle
    def delete_mid(self, index: int) -> None:
        self.deque.pop(index)

    # delete the value at the tail
    def delete_tail(self) -> None:
        self.deque.pop()

    # get the memory usage
    def memory_usage(self) -> int:
        return sys.getsizeof(self.deque)

# ------------------------------------------------------------------- #
