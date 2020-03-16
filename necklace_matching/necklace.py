class Node:
    def __init__(self, char, prev, succ):
        self.succ = succ
        self.prev = prev
        self.current = char

    def __eq__(self, obj):
        return isinstance(obj, Node) and \
               self.current == obj.current and \
               self.succ == obj.succ and \
               self.prev == obj.prev

    def __hash__(self):
        return hash(self.current + self.succ + self.prev)


class Necklace:
    def __init__(self, string):
        self.nodes = {}

        for i in range(len(string)):
            current = string[i]
            prev = string[i - 1]
            if i == len(string) - 1:
                succ = string[0]
            else:
                succ = string[i + 1]
            node = Node(current, prev, succ)
            if node in self.nodes:
                self.nodes[node] = self.nodes[node] + 1
            else:
                self.nodes[node] = 1

    def __eq__(self, obj):
        if not isinstance(obj, Necklace):
            return False
        return self.nodes == obj.nodes

    def __hash__(self):
        result = []
        result_hash = ""
        for node in self.nodes:
            result.append(node.__hash__())
        result = sorted(result)
        for node in result:
            result_hash += str(node)
        return hash(result_hash)
