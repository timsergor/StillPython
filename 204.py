# 622. Design Circular Queue. Medium. 40.9%.

# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Your implementation should support following operations:

# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.

def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.stack = {i:"*" for i in range(k)}
        self.head = 0
        self.tail = 0
        self.length = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.head - self.tail == self.length - 1:
            return False
        else:
            self.head += 1
            self.stack[self.head] = value  
            if self.head == self.tail + 1 and self.stack[self.tail] == "*":
                self.tail += 1
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.tail not in self.stack or self.stack[self.tail] == "*":
            return False
        else:
            x = self.stack[self.tail]
            self.stack[self.tail] = "*"
            self.tail += 1
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.stack[self.tail] == "*":
            return -1
        else:
            return self.stack[self.tail]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.stack[self.head] == "*":
            return -1
        else:
            return self.stack[self.head]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.stack[self.head] == "*"

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.head - self.tail == self.length - 1

# 50-60min.
