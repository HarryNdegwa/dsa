class Node(object):

    def __init__(self,value):
        self.value = value
        self.next_node = None


class LinkedList(object):

    def __init__(self,head=None):
        if head:
            self.head = Node(head)
        else:
            self.head = None


    def insert_start(self,value):
        if self.head == None:
            self.head == Node(value)
        else:
            current_head = self.head
            self.head = Node(value)
            self.head.next_node = current_head


    def insert_end(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            self._insert(self.head,value)


    def _insert(self,current_node,value):
        if current_node.next_node == None:
            current_node.next_node = Node(value)
        else:
            self._insert(current_node.next_node,value)


    def delete(self,value):
        if self.head == None:
            return 
        elif self.head.value == value:
            self.head = self.head.next_node
        else:
            self._delete(self.head,value)


    def _delete(self,current_node,value):
        if current_node.value == value:
            current_node = current_node.next_node
        else:
            self._delete(current_node.next_node,value)


    def print_list(self):
        if not self.head:
            print("Empty!!")
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next_node



    def search(self,value):
        if not self.head:
            return "Empty!!"
        return self._search(self.head,value)


    def _search(self,current_node,value):
        if current_node == None:
            return 
        elif current_node.value == value:
            return current_node.next_node.value
        return self._search(current_node.next_node,value)


    def size(self):
        if self.head == None:
            return 0
        count_ = 0
        current = self.head
        while current:
            count_+=1
            current = current.next_node
        return count_


if __name__ == "__main__":
    l = LinkedList(1)
    l.insert_end(2)
    l.insert_end(3)
    l.insert_end(4)
    l.insert_start(0)
    l.insert_start(10)
    l.insert_start(100)
    l.print_list()
    print(l.size())


    
               




