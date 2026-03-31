class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1) # Dummy Node, its function is keep head active  
        self.tail = self.head # -> At the start, head and tail point to the same Node
    
    def get(self, index: int) -> int:
        current = self.head.next
        counter = 0
        while current != None:
            if counter == index:
                return current.value
            counter += 1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
        if new_node.next == None:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

        

    def remove(self, index: int) -> bool:
        current = self.head
        counter = 0
        while current and counter < index:
            counter += 1
            current = current.next
        if current != None and current.next != None:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False
            
        

    def getValues(self) -> List[int]:
        empt_list = []
        current = self.head.next
        while current != None:
            empt_list.append(current.value)
            current = current.next
        return empt_list
        
