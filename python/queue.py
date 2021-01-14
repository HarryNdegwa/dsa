class Queue(object):

    def __init__(self,size):
        self.queue = []
        self.size = size


    def enqueue(self,value):
        if self.isFull():
            return 
        self.queue.append(value)


    def dequeue(self):
        if self.isEmpty():
            return 
        self.queue.remove(self.queue[0])


    def isEmpty(self):
        return self.queue == []


    def isFull(self):
        return len(self.queue) == self.size


    def peek(self):
        return self.queue[0]


    def print_queue(self):
        print(self.queue)



if __name__ == "__main__":
    q = Queue(7)
    print(q.isFull())
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.print_queue()
    print(q.isFull())
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.print_queue()
    print(q.isFull())
    print(q.isEmpty())
    print(q.peek())
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.print_queue()
    print(q.isFull())
    print(q.isEmpty())
    print(q.peek())



