class Stack(object):

    def __init__(self,size):
        self.stack = []
        self.size = size


    def push(self,value):
        if self.isFull():
            return
        self.stack.insert(0,value)


    def pop(self):
        if self.isEmpty():
            return 
        self.stack.remove(self.stack[0])


    def peek(self):
        return self.stack[0]


    def isEmpty(self):
        return self.stack == []

    def isFull(self):
        return len(self.stack)==self.size


    def print_stack(self):
        print(self.stack)



if __name__ == '__main__':
    s = Stack(10)
    print(s.isEmpty())
    print(s.isFull())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.print_stack()
    print(s.isEmpty())
    print(s.isFull())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.print_stack()
    print(s.isEmpty())
    print(s.isFull())
    s.pop()
    s.pop()
    s.pop()
    s.print_stack()
    print(s.isEmpty())
    print(s.isFull())