class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty!")

    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            raise IndexError("Queue is full!")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty!")


my_queue = Queue(capacity=5)
my_queue.enqueue(10)
my_queue.enqueue(20)
print(my_queue.front())
my_queue.dequeue()
print(my_queue.front())
