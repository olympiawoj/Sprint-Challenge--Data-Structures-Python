from doubly_linked_list import DoublyLinkedList

"""
- Non-growable, fixed size

- append --> #Adds elements to the buffer
- When full, the OLDEST el is overwritten by a new el
Check for length of storage vs capacity - 

- get --> #returns all elements in the buffer in order, do not return any NONE values in list even if present in buffer

We are using a DLL for storage

In this example, head is the last added item
Tail is the most recently added item 

"""

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None #where head of ring is currently located
        self.storage = DoublyLinkedList()
        self.length = self.storage.length

    def append(self, item):
        #if storage is 0, initiate ring
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            #set current to that item
            self.current = self.storage.head

        #if at capacity and current is NOT at head. remove from head & add to tail
        elif self.storage.length == self.capacity and not self.current is self.storage.head:
            #remove the head and add to tail item
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
        #if at capacity and current is at head (end of list)
        elif self.storage.length == self.capacity:
            #remove item the head and add to tail item
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            #set current to tail
            self.current = self.storage.tail
        #if not at capacity, add to tail
        else:
            self.storage.add_to_tail(item)
           
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # if self.current is None:
        #     return list_buffer_contents
        while len(list_buffer_contents) < self.storage.length:
            list_buffer_contents.append(self.current.value)
            #if there is next, set current to next
            if self.current.next:
                self.current = self.current.next
            else:
                #set current to head
                self.current = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

# buffer = RingBuffer(3)
# print("Print Buffer get() ---> ", buffer.get())        # []
# buffer.append('a')

# print("Print Buffer get() ---> ", buffer.get())        # 1 ['a']
# buffer.append('b')
# print("Print Buffer get() ---> ", buffer.get())        # 2 ['a', 'b']
# buffer.append('c')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['a', 'b', 'c']
# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['d', 'b', 'c']
# buffer.append('e')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['d', 'e', 'c']
# buffer.append('f')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['d', 'e', 'f']
# buffer.append('g')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['g', 'e', 'f']
# buffer.append('h')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['g', 'h', 'f']
# buffer.append('i')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['g', 'h', 'i']
