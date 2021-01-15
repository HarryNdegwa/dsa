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

