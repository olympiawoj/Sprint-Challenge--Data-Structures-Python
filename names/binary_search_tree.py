from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

"""
PLAN

Use recursion
Steps - Iteratively or Recursively

- Starting at the root
    - Check if there is a root. If not, the root becomes that new node!
    - If there is a root, check if the value of the new node is greater than or less than the value of the root
    - **If it is less**
        - Check to see if there's a node to the left
            - If there is, move that node and repeat these steps
            - If there is not, add that node as the left property
    - **If it is greater**
        - Check to see if there's a node to the right
            - If there is, move to that node and repeat these steps
            - If there is not, add that ndoe as the right property
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # print("\ninserting value:", value)
        # print("\nstarting values:", "val:", self.value,
        #       "left:", self.left, "right:", self.right)

        # # If value is the same as the root, return undefined
        # if value == self.value:
        #     return None

        bst = BinarySearchTree(value)
        # If value is less than self.value
        if value < self.value:
            # Is there a node to the left?
            if self.left is None:
                self.left = bst
            else:
                # If so, recurse
                self.left.insert(value)
        # If value is greater than self.value
        else:
            # Is there a node to the right?
            if self.right is None:
                # If not, add that node as the left property
                self.right = bst
            else:
                # If so, recurse
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Base Case
        if self.value == target:
            return True

        if self.left is None and self.right is None:
            return False
        if target < self.value:
            return self.left.contains(target)
        if target >= self.value:
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # If there's nothing to the right, return self.value
        if self.right is None:
            return self.value
        # Else, recurse
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    """
1) call cb on self.value
2) if left, call it
3) if right, call it
returns - two types of recursion problems. One goes outward and does something along the way - could be calling a function, and when it gets to the end it's done. Can tell if its trying to DO something or create something. In that case, don't need a return cb don't need any data. BUT if the spec says return, we need to return our recursive calls instead of just calling

breadth first - queue- FIFO
depth first - stack

    """

    def for_each(self, cb):
        cb(self.value)
        # If there's a left, call for_each and if there's a right, call for_each.
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)


# Print the value of every node, starting with the given node,
# in an iterative breadth first traversal

# We need to create a Queue using our imported Queue class and then use methods on that class
# methods - len, enqueue, and dequeue
#    * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.


    def bft_print(self, node):
        # create queue using import
        self.queue = Queue()
        # add node to back of queue
        self.queue.enqueue(node)
        # if there is ANYTHING in the queue,

        while(self.queue.len() is not 0):
            # remove something from beginning of queue and assign it to node
            node = self.queue.dequeue()
            # is there a left or right?   # if so, remove and return item from front of queue
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            print(node.value)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal
        # iterative means Don't use recursion!
        # Our Stack has push and pop methods - push adds to the top, pop takes off from the top

    def dft_print(self, node):
        stack = Stack()
        # push node to top of stack
        stack.push(node)
        # while len of stack is greater than 0
        while stack.len() != 0:
            # remove node from top
            node = stack.pop()
            if node.left:
                stack.push(node.left)
                # print('left', node.value)
            if node.right:
                stack.push(node.right)
            print(node.value)
            # print('right', node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.print_values()
# bst.in_order_print(bst)
# print("\nContains :", bst.contains(4))  # true

tree = BinarySearchTree(5)
tree.insert(2)
tree.insert(7)
# tree.insert(3)
# tree.insert(8)
# tree.insert(20)

# should be 3, 6, 8, 10, 15, 20
print('printing depth in order')
tree.in_order_print(tree)

# should be 10, 6, 15, 3, 8, 20
print('printing breadth first')
tree.bft_print(tree)

# 5
# 2 #7

# root node, value 2, 5, 7

# should be 3, 6, 8, 10, 15, 20
print('printing depth iteratively')
tree.dft_print(tree)
