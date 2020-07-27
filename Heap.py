

class heap:
    def __init__(self, value):
        self.array = [value]

    def leftChildIndex(self, parent):
        index = 2 * parent + 1
        if index >= len(self.array):
            return None
        return index
    
    def rightChildIndex(self, parent):
        index = 2 * parent + 2
        if index >= len(self.array):
            return None
        return index

    def parentIndex(self, child):
        index = (child - 1) // 2
        if index < 0:
            return None
        return index

    def parent(self, child):
        index = self.parentIndex(child)
        if index is None:
            return None
        return self.array[index]
        
    def peek(self):
        if not self.array:
            return None
        return self.array[0]
    
    def poll(self):
        if not self.array:
            return None
        array = self.array
        top = array[0]
        array[0] = array[len(array)-1]
        del array[len(array)-1]
        self.heapifyDown()
        return top

    def add(self, value):
        self.array.append(value)
        self.heapifyUp()
        return self

    def heapifyDown(self):
        array = self.array
        i = 0
        while True:
            l = self.leftChildIndex(i)
            r = self.rightChildIndex(i)
            if l is None and r is None:
                break
            elif l is not None and r is not None:
                minChild = min(l, r)
            elif l is not None: # r is None
                minChild = l
            else: # else l is None; this should *not* happen
                assert False, "Error: Right child exists without left child."
            # swap if needed
            if array[minChild] < array[i]:
                array[minChild], array[i] = array[i], array[minChild]
                i = minChild
            else:
                break

    def heapifyUp(self):
        array = self.array
        i = len(array)-1
        p = self.parentIndex(i)
        while p is not None:
            if array[i] >= array[p]:
                break
            # else swap
            array[i], array[p] = array[p], array[i]
            i = p
            p = self.parentIndex(i)
    
    def print(self):
        print(self.array)

    def printTree(self):
        array = self.array
        queue = [0]
        nextq = []
        while len(queue) > 0:
            i = queue.pop(0)            
            print(array[i], end=" ")
            left = self.leftChildIndex(i)
            if left:
                nextq.append(left)
            right = self.rightChildIndex(i)
            if right:
                nextq.append(right)
            if len(queue) == 0:
                print()
                queue = nextq[:]
                nextq = []

            


myHeap = heap(2)
assert myHeap.array == [2]
myHeap.add(4).add(8).add(9).add(7).add(10).add(9).add(15).add(20).add(13)
assert myHeap.array == [2, 4, 8, 9, 7, 10, 9, 15, 20, 13]
myHeap.print()
myHeap.add(1)
assert myHeap.array == [1, 2, 8, 9, 4, 10, 9, 15, 20, 13, 7]
myHeap.print()
myHeap.printTree()
assert myHeap.peek() == 1
assert myHeap.poll() == 1
myHeap.print()
assert myHeap.array == [2, 7, 8, 9, 4, 10, 9, 15, 20, 13]
assert myHeap.peek() == 2
myHeap.print()
myHeap.printTree()