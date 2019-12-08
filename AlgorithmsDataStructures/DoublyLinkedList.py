class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head == self.tail:
            return
        self.remove(nodeToInsert)
        if node.prev is not None:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
        node.prev = nodeToInsert
        nodeToInsert.next = node
        if node is self.head:
            self.head = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head == self.tail:
            return
        self.remove(nodeToInsert)
        if node.next is not None:
            node.next.prev = nodeToInsert
            nodeToInsert.next = node.next
        node.next = nodeToInsert
        nodeToInsert.prev = node
        if node is self.tail:
            self.tail = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        currentNode = self.head
        currentPosition = 1
        while currentNode is not None and currentPosition < position:
            currentNode = currentNode.next
            currentPosition += 1
        if currentNode is not None:
            self.insertBefore(currentNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            nodeToRemove = current
            current = current.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def printList(self):
        printString = "{"
        current = self.head
        while current is not None:
            printString += f" {current.value},"
            current = current.next
        printString += f" head: {self.head.value}, tail: {self.tail.value} }}"
        print(printString)


if __name__ == "__main__":
    link = DoublyLinkedList()
    first, second = Node(25), Node(30)
    link.setHead(first)
    # link.printList()
    # link.setTail(second)
    link.printList()
    link.insertBefore(first, second)
    link.printList()
