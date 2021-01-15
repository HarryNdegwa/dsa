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

    
