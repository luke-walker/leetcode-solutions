class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.rear = None
        self.size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.head is None:
            self.head = Node(value)
            self.rear = self.head
        else:
            node = Node(value, next=self.head)
            self.head.prev = node
            self.head = node

        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.rear is None:
            self.rear = Node(value)
            self.head = self.rear
        else:
            node = Node(value, prev=self.rear)
            self.rear.next = node
            self.rear = node

        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.head is None:
            return False

        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
            if self.head.next is None:
                self.rear = self.head
        else:
            self.rear = None

        self.size -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.rear is None:
            return False

        self.rear = self.rear.prev
        if self.rear is not None:
            self.rear.next = None
            if self.rear.prev is None:
                self.head = self.rear
        else:
            self.head = None
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.head is not None else -1
        
    def getRear(self) -> int:
        return self.rear.val if self.rear is not None else -1
        
    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.max_size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
