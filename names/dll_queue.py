

from doubly_linked_list import DoublyLinkedList
import sys
print(sys.path)
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Efficient
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add to head, increase size, return size
        self.storage.add_to_head(value)
        self.size += 1
        return self.size

    def dequeue(self):
        # Check to see if the list length is less than or 0
        # If zero, can't allow dequeue
        if self.size <= 0:
            return None
        # Decrease size by 1
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
