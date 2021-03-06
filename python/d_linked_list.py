class Node(object):

    def __init__(self,value):
        self.value = value
        self.prev_node = None
        self.next_node = None



class DoublyLinkedList(object):

    def __init__(self,head=None):
        if head:
            self.head = Node(head)
        else:
            self.head = None



    def insert_start(self,value):
        if self.head:
            head = self.head
            self.head = Node(value)
            self.head.next_node = head
        else:
            self.head = Node(value)


    def insert_center(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            center = round(self.size()/2)
            self._insert_center(self.head,value,center)


    def _insert_center(self,current_node,value,center,count=1):
        if center == count:
            next_ = current_node.next_node
            current_node.next_node = Node(value)
            current_node.next_node.next_node = next_
        else:
            self.insert_center(current_node.next_node,value,center,count+1)



    def insert_end(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            self._insert_end(self.head,value)



    def _insert_end(self,current_node,value):
        if not current_node.next_node:
            current_node.next_node = Node(value)
        else:
            self._insert_end(current_node.next_node,value)


    def size(self):
        if not self.head:
            return 0
        count_ = 0
        current = self.head
        while current:
            count_+=1
            current = current.next_node
        return count_


    def traverse(self):
        if self.head == None:
            print("Empty!!")
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next_node




if __name__ == "__main__":
    l = DoublyLinkedList(1)
    l.insert_start(0)
    l.insert_center(2)
    l.insert_end(3)
    l.traverse()




    


    
