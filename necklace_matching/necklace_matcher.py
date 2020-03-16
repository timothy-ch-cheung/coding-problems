class Node:
    def __init__(self, char):
        self.next = None
        self.prev = None
        self.current = char

    def __eq__(self, obj):
        return isinstance(obj, Node) and \
               self.current == obj.current and \
               self.next.current == obj.next.current and \
               self.prev.current == obj.prev.current

    def __hash__(self):
        if self.prev is not None and self.next is not None:
            return hash(self.current)
        else:
            return hash(self.current, self.next.current, self.prev.current)


class Necklace:
    def __init__(self, string):
        self.length = len(string)
        links = []
        for letter in string:
            links.append(Node(letter))
        for i in range(len(links)):
            if i == len(links) - 1:
                links[i].next = links[0]
            else:
                links[i].next = links[i + 1]
            links[i].prev = links[i - 1]

        self.nodes = set(links)

    def __eq__(self, obj):
        if not isinstance(obj, Necklace) or self.length != obj.length:
            return False
        else:
            for node in self.nodes:
                if node not in obj.nodes:
                    return False
        return True


def same_necklace(string_a, string_b):
    necklace_a = Necklace(string_a)
    necklace_b = Necklace(string_b)
    return necklace_a == necklace_b
