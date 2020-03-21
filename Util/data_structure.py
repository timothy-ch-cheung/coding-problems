class Node:

    def __init__(self, char):
        self.current = char
        self.prev = None
        self.succ = None

    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, succ):
        self.succ = succ


class CircularList:

    def __init__(self):
        self.nodes = []
        self.size = 0

    def add(self, char):
        node = Node(char)
        if (self.size == 0):
            node.set_next(node)
            node.set_next(node)
        else:
            node.set_next(node[0])
            node.set_prev(node[len(self.nodes) - 1])
            node[0].set_prev(node)
            node[len(self.nodes) - 1].set_next(node)
        self.nodes.append(node)
        self.size += 1
