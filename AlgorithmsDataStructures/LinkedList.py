class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if head is None:
            head = Node(data)
            return
        currentNode = head
        while currentNode is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        oldHead = head
        head = Node(data)
        head.next = oldHead

    def deleteValue(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            nodeToDelete = self.head
            self.head = self.head.next
            del nodeToDelete
            return
        currentNode = self.head
        while currentNode.next is not None:
            if currentNode.next.data == data:
                # found node to delete
                nodeToDelete = currentNode.next
                currentNode.next = currentNode.next.next
                del nodeToDelete
                return
            currentNode = currentNode.next


if __name__ == "__main__":
    pass
