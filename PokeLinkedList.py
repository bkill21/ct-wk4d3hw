from Node import Node

class PokeLinkedList():

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.value)
        return ' -> '.join(nodes)


    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.right:
                current_node = current_node.right
            current_node.right = node