class Node:

    def __init__(self, freq, prev=None, next=None):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.rear = Node(0)
        self.head.next = self.rear
        self.rear.prev = self.head
        self.node_map = {}

    def _is_empty(self) -> bool:
        return self.head.next == self.rear

    def inc(self, key: str) -> None:
        if key not in self.node_map:
            if self.head.next.freq != 1:
                node = Node(1, prev=self.head, next=self.head.next)
                node.keys.add(key)
                self.head.next.prev = node
                self.head.next = node
                self.node_map[key] = node
            else:
                self.head.next.keys.add(key)
                self.node_map[key] = self.head.next
        else:
            curr = self.node_map[key]
            curr.keys.remove(key)
            if curr.next.freq == curr.freq+1:
                curr.next.keys.add(key)
                self.node_map[key] = curr.next
            else:
                node = Node(curr.freq+1, prev=curr, next=curr.next)
                node.keys.add(key)
                curr.next.prev = node
                curr.next = node
                self.node_map[key] = node
            if len(curr.keys) == 0:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev

    def dec(self, key: str) -> None:
        if self._is_empty() or key not in self.node_map:
            return

        curr = self.node_map[key]
        self.node_map[key].keys.remove(key)
        if curr.freq == 1:
            del self.node_map[key]
        else:
            if curr.prev.freq == curr.freq-1:
                curr.prev.keys.add(key)
                self.node_map[key] = curr.prev
            else:
                node = Node(curr.freq-1, prev=curr.prev, next=curr)
                node.keys.add(key)
                curr.prev.next = node
                curr.prev = node
                self.node_map[key] = node
        if len(curr.keys) == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

    def getMaxKey(self) -> str:
        if self._is_empty():
            return ""
        for key in self.rear.prev.keys:
            return key

    def getMinKey(self) -> str:
        if self._is_empty():
            return ""
        for key in self.head.next.keys:
            return key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
