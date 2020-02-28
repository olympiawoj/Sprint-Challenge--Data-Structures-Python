"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    """
    We cannot do len(my_linked_list)
    The reason we can do that for an array and it returns a value is bc Python programmed that

    """

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # Add to the length
        self.length += 1
        # Special case:
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            # Update new node.next to current head
            # new_node.next = self.head
            # # self.head.prev = new_node
            #    self.head = new_node
            self.head.insert_before(value)
            self.head = self.head.prev

            # What do we need to think about? What are the scenarios?
            # This needs to be head bc we're adding to the head
            # Update previous head
            # Increase length
            # Edge cases - if self.head is none, then there is no list no tail
            # If there's no tail.. New head becomes new tail

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # Add to tail is similar to add to head
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tial
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if node is self.head:
        #     return
        # value = node.value
        # if node is self.tail:
        #     self.remove_from_tail()
        # else:
        #     node.delete()
        # self.add_to_head(value)

        self.delete(node)
        # Node exists, we're not cutting it loos, but eventually garabge collection will get it, pointer untouched, object there just nothing pointing to it
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # Need tedge cases for deleting head, deleting tail, or deleting the only element

        # If LL is empty
        if not self.head and not self.tail:
            print("ERROR: Attempted to delete node not in list")
            return
        # If node is both- this gets triggered BEFORE our if node is head
        # Don't need to delete the node here bc garb collection takes care of it
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # If node is head
        elif node == self.head:

            self.head = self.head.next
            node.delete()
        # If node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()

            # If node is in middle
        else:
            node.delete()

        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        #Plan:#
        # Make max var
        # Lopo through nodes via node.next
        # If node.value is higher, update max
        # return max
        pass
