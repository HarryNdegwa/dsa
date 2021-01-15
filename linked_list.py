class Node(object):

    def __init__(self,value):
        self.value = value
        self.next_node:None


class LinkedList(object):

    def __init__(self,head=None):
        if head:
            self.head = Node(head)
        else:
            self.head = None


    def insert(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            self._insert(self.head,value)


    def _insert(self,current_node,value):
        if current_node.next_node == None:
            current_node.next_node = Node(value)
        else:
            self._insert(current_node.next_node,value)

