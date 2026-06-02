class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:   
        if index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next 
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        prev = self.head
        current = prev.next
        for i in range(index-1):
            prev = current
            current = current.next
        prev.next = current.next
        self.size -= 1
        return True
        
    def getValues(self) -> List[int]:
        current = self.head
        result = []
        for i in range(self.size):
            result.append(current.val)
            current = current.next
        return result


        