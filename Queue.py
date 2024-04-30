class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        value = self.head.value
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.value
    
def test_queue():
    queue = Queue(max_size=5)

    # Enqueue elements
    for i in range(1, 6):
        queue.enqueue(i)
    print("Enqueued elements:", end=" ")
    while not queue.is_empty():
        print(queue.dequeue(), end=" ")
    print()

    # Test isEmpty
    print("Is the queue empty?", queue.is_empty())

    # Test isFull
    print("Is the queue full?", queue.is_full())

    # Test Peek
    queue.enqueue(10)
    print("Peek:", queue.peek())

test_queue()