class Node:


def __init__(self, data) -> None:
    self.data = data
    self.next = None



    class Stack():
        def __init__(self) -> None:
            self.top = None
            self.size = 0


            def push(self, node):
                 node.next = self.top
                 self.top = node 
                 self.size += 1